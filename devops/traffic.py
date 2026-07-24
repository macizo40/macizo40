import boto3

REGION = "us-east-1"
AZ1 = "us-east-1a"
TARGET_GROUP_ARN = "arn:aws:elasticloadbalancing:us-east-1:111122223333:targetgroup/myTG/abcdef"

ec2 = boto3.client("ec2", region_name=REGION)
elbv2 = boto3.client("elbv2", region_name=REGION)

reservations = ec2.describe_instances(
    Filters=[
        {"Name": "availability-zone", "Values": [AZ1]},
        {"Name": "instance-state-name", "Values": ["running"]},
    ]
)["Reservations"]

targets = []

for reservation in reservations:
    for instance in reservation["Instances"]:
        targets.append({"Id": instance["InstanceId"]})

if targets:
    elbv2.deregister_targets(
        TargetGroupArn=TARGET_GROUP_ARN,
        Targets=targets
    )
    print("Traffic shifted to AZ2.")
else:
    print("No instances found in AZ1.")