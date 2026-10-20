
import boto3
import json
import argparse
from datetime import datetime, timedelta, timezone
from botocore.exceptions import ClientError, BotoCoreError

def aws_client(service, region=None):
    return boto3.client(service, region_name=region)

def metric_average(cw, namespace, metric, dimensions, hours=24):
    end = datetime.now(timezone.utc)
    start = end - timedelta(hours=hours)

    try:
        result = cw.get_metric_statistics(
            Namespace=namespace,
            MetricName=metric,
            Dimensions=dimensions,
            StartTime=start,
            EndTime=end,
            Period=3600,
            Statistics=["Average"]
        )
        points = result.get("Datapoints", [])
        if not points:
            return None
        return round(
            sum(p["Average"] for p in points) / len(points), 2
        )
    except (ClientError, BotoCoreError) as exc:
        print(f"Metric unavailable: {metric}: {exc}")
        return None

def get_regions():
    ec2 = aws_client("ec2", "us-east-1")
    response = ec2.describe_regions(AllRegions=False)
    return [r["RegionName"] for r in response["Regions"]]

def ec2_usage(region):
    ec2 = aws_client("ec2", region)
    cw = aws_client("cloudwatch", region)
    records = []

    for page in ec2.get_paginator(
        "describe_instances"
    ).paginate():
        for reservation in page["Reservations"]:
            for instance in reservation["Instances"]:
                iid = instance["InstanceId"]
                state = instance["State"]["Name"]

                cpu = None
                if state == "running":
                    cpu = metric_average(
                        cw, "AWS/EC2", "CPUUtilization",
                        [{"Name": "InstanceId", "Value": iid}]
                    )

                records.append({
                    "instance_id": iid,
                    "type": instance["InstanceType"],
                    "state": state,
                    "cpu_average_percent": cpu,
                    "vpc_id": instance.get("VpcId")
                })

    return records

def ebs_usage(region):
    ec2 = aws_client("ec2", region)
    records = []

    for page in ec2.get_paginator(
        "describe_volumes"
    ).paginate():
        for volume in page["Volumes"]:
            records.append({
                "volume_id": volume["VolumeId"],
                "size_gb": volume["Size"],
                "type": volume["VolumeType"],
                "state": volume["State"],
                "attached": bool(volume.get("Attachments"))
            })

    return records

def rds_usage(region):
    rds = aws_client("rds", region)
    cw = aws_client("cloudwatch", region)
    records = []

    for page in rds.get_paginator(
        "describe_db_instances"
    ).paginate():
        for db in page["DBInstances"]:
            dbid = db["DBInstanceIdentifier"]

            cpu = metric_average(
                cw, "AWS/RDS", "CPUUtilization",
                [{"Name": "DBInstanceIdentifier",
                  "Value": dbid}]
            )

            records.append({
                "database": dbid,
                "engine": db["Engine"],
                "class": db["DBInstanceClass"],
                "status": db["DBInstanceStatus"],
                "cpu_average_percent": cpu,
                "allocated_storage_gb":
                    db.get("AllocatedStorage")
            })

    return records

def lambda_usage(region):
    client = aws_client("lambda", region)
    cw = aws_client("cloudwatch", region)
    records = []

    for page in client.get_paginator(
        "list_functions"
    ).paginate():
        for function in page["Functions"]:
            name = function["FunctionName"]

            records.append({
                "function": name,
                "runtime": function.get("Runtime"),
                "memory_mb": function["MemorySize"],
                "invocations_average": metric_average(
                    cw, "AWS/Lambda", "Invocations",
                    [{"Name": "FunctionName", "Value": name}]
                )
            })

    return records

def ecs_usage(region):
    ecs = aws_client("ecs", region)
    records = []

    for page in ecs.get_paginator(
        "list_clusters"
    ).paginate():
        arns = page.get("clusterArns", [])
        for i in range(0, len(arns), 100):
            clusters = ecs.describe_clusters(
                clusters=arns[i:i+100]
            ).get("clusters", [])

            for cluster in clusters:
                records.append({
                    "cluster": cluster["clusterName"],
                    "status": cluster["status"],
                    "running_tasks":
                        cluster["runningTasksCount"],
                    "pending_tasks":
                        cluster["pendingTasksCount"],
                    "active_services":
                        cluster["activeServicesCount"]
                })

    return records

def eks_usage(region):
    eks = aws_client("eks", region)
    records = []

    for page in eks.get_paginator(
        "list_clusters"
    ).paginate():
        for name in page["clusters"]:
            cluster = eks.describe_cluster(
                name=name
            )["cluster"]

            records.append({
                "cluster": name,
                "version": cluster["version"],
                "status": cluster["status"]
            })

    return records

def elb_usage(region):
    elb = aws_client("elbv2", region)
    records = []

    for page in elb.get_paginator(
        "describe_load_balancers"
    ).paginate():
        for lb in page["LoadBalancers"]:
            records.append({
                "name": lb["LoadBalancerName"],
                "type": lb["Type"],
                "state": lb["State"]["Code"],
                "scheme": lb["Scheme"]
            })

    return records

def s3_usage():
    s3 = aws_client("s3", "us-east-1")
    records = []

    for bucket in s3.list_buckets().get("Buckets", []):
        records.append({
            "bucket": bucket["Name"],
            "created": bucket["CreationDate"].isoformat()
        })

    return records

def monthly_cost():
    ce = aws_client("ce", "us-east-1")
    now = datetime.now(timezone.utc)

    start = now.replace(day=1).date().isoformat()
    end = (now.date() + timedelta(days=1)).isoformat()

    result = ce.get_cost_and_usage(
        TimePeriod={"Start": start, "End": end},
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
        GroupBy=[{
            "Type": "DIMENSION",
            "Key": "SERVICE"
        }]
    )

    costs = []
    for period in result["ResultsByTime"]:
        for group in period["Groups"]:
            amount = group["Metrics"]["UnblendedCost"]
            costs.append({
                "service": group["Keys"][0],
                "amount": round(float(amount["Amount"]), 2),
                "currency": amount["Unit"]
            })

    return sorted(
        costs, key=lambda x: x["amount"], reverse=True
    )

def collect_safely(name, function, *args):
    try:
        return function(*args)
    except (ClientError, BotoCoreError) as exc:
        print(f"ERROR collecting {name}: {exc}")
        return {"error": str(exc)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", default="all")
    parser.add_argument(
        "--output", default="aws_infrastructure_report.json"
    )
    args = parser.parse_args()

    regions = (
        get_regions() if args.region == "all"
        else [args.region]
    )

    report = {
        "generated_at":
            datetime.now(timezone.utc).isoformat(),
        "regions": {},
        "s3": collect_safely("S3", s3_usage),
        "monthly_cost": collect_safely(
            "Cost Explorer", monthly_cost
        )
    }

    services = {
        "ec2": ec2_usage,
        "ebs": ebs_usage,
        "rds": rds_usage,
        "lambda": lambda_usage,
        "ecs": ecs_usage,
        "eks": eks_usage,
        "load_balancers": elb_usage
    }

    for region in regions:
        print(f"Scanning region: {region}")
        report["regions"][region] = {}

        for name, function in services.items():
            report["regions"][region][name] = (
                collect_safely(name, function, region)
            )

    with open(args.output, "w") as file:
        json.dump(report, file, indent=2)

    print(f"Report generated: {args.output}")

if __name__ == "__main__":
    main()
