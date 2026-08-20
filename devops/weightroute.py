import boto3

route53 = boto3.client("route53")

HOSTED_ZONE_ID = "Z1234567890ABC"
DOMAIN = "app.example.com"

DC1_IP = "203.0.113.10"
DC2_IP = "203.0.113.20"

def configure_50_50():

    # Data Center 1
    route53.change_resource_record_sets(
        HostedZoneId=HOSTED_ZONE_ID,
        ChangeBatch={
            "Changes": [{
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": DOMAIN,
                    "Type": "A",
                    "SetIdentifier": "DC1",
                    "Weight": 50,
                    "TTL": 30,
                    "ResourceRecords": [
                        {"Value": DC1_IP}
                    ]
                }
            }]
        }
    )

    # Data Center 2
    route53.change_resource_record_sets(
        HostedZoneId=HOSTED_ZONE_ID,
        ChangeBatch={
            "Changes": [{
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": DOMAIN,
                    "Type": "A",
                    "SetIdentifier": "DC2",
                    "Weight": 50,
                    "TTL": 30,
                    "ResourceRecords": [
                        {"Value": DC2_IP}
                    ]
                }
            }]
        }
    )

    print("Traffic configured for 50% DC1 / 50% DC2")


if __name__ == "__main__":
    configure_50_50()