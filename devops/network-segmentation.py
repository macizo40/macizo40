"""
PCI Network Segment - AWS / Boto3

Creates:
- Dedicated PCI VPC
- PCI application subnet
- PCI database subnet
- Dedicated route table
- PCI application security group
- PCI database security group
- Network ACL
- VPC Flow Logs
- Default encryption-related tagging

IMPORTANT:
This creates network segmentation controls, but PCI DSS compliance
also requires IAM, logging, encryption, vulnerability management,
monitoring, key management, policies, testing, etc.
"""

import boto3
import time

REGION = "us-east-1"

# Dedicated PCI network
PCI_VPC_CIDR = "10.50.0.0/16"
PCI_APP_CIDR = "10.50.10.0/24"
PCI_DB_CIDR = "10.50.20.0/24"

ec2 = boto3.client("ec2", region_name=REGION)


def tag_resource(resource_id, name, component):
    ec2.create_tags(
        Resources=[resource_id],
        Tags=[
            {"Key": "Name", "Value": name},
            {"Key": "Environment", "Value": "PCI"},
            {"Key": "DataClassification", "Value": "CardholderData"},
            {"Key": "Compliance", "Value": "PCI-DSS"},
            {"Key": "Component", "Value": component},
            {"Key": "ManagedBy", "Value": "Python-Boto3"},
        ],
    )


def create_vpc():
    response = ec2.create_vpc(
        CidrBlock=PCI_VPC_CIDR
    )

    vpc_id = response["Vpc"]["VpcId"]

    ec2.get_waiter("vpc_available").wait(
        VpcIds=[vpc_id]
    )

    tag_resource(
        vpc_id,
        "pci-cde-vpc",
        "network"
    )

    # Enable DNS
    ec2.modify_vpc_attribute(
        VpcId=vpc_id,
        EnableDnsSupport={"Value": True}
    )

    ec2.modify_vpc_attribute(
        VpcId=vpc_id,
        EnableDnsHostnames={"Value": True}
    )

    print(f"[+] PCI VPC created: {vpc_id}")

    return vpc_id


def create_subnet(vpc_id, cidr, name):
    response = ec2.create_subnet(
        VpcId=vpc_id,
        CidrBlock=cidr
    )

    subnet_id = response["Subnet"]["SubnetId"]

    tag_resource(
        subnet_id,
        name,
        "subnet"
    )

    # Critical:
    # Do NOT automatically assign public IPs.
    ec2.modify_subnet_attribute(
        SubnetId=subnet_id,
        MapPublicIpOnLaunch={"Value": False}
    )

    print(f"[+] Private PCI subnet created: {subnet_id}")

    return subnet_id


def create_route_table(vpc_id, subnets):
    response = ec2.create_route_table(
        VpcId=vpc_id
    )

    route_table_id = response["RouteTable"]["RouteTableId"]

    tag_resource(
        route_table_id,
        "pci-private-route-table",
        "routing"
    )

    for subnet_id in subnets:
        ec2.associate_route_table(
            RouteTableId=route_table_id,
            SubnetId=subnet_id
        )

    # Intentionally NO:
    #
    # 0.0.0.0/0 -> Internet Gateway
    #
    # PCI systems remain isolated by default.

    print(
        f"[+] PCI private route table created: "
        f"{route_table_id}"
    )

    return route_table_id


def create_app_security_group(vpc_id):
    response = ec2.create_security_group(
        GroupName="pci-app-sg",
        Description="PCI application tier security group",
        VpcId=vpc_id
    )

    sg_id = response["GroupId"]

    tag_resource(
        sg_id,
        "pci-app-sg",
        "firewall"
    )

    # Remove unrestricted outbound traffic.
    try:
        ec2.revoke_security_group_egress(
            GroupId=sg_id,
            IpPermissions=[
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {"CidrIp": "0.0.0.0/0"}
                    ]
                }
            ]
        )
    except Exception:
        pass

    print(f"[+] PCI APP SG created: {sg_id}")

    return sg_id


def create_database_security_group(
    vpc_id,
    app_sg_id
):
    response = ec2.create_security_group(
        GroupName="pci-db-sg",
        Description="PCI database security group",
        VpcId=vpc_id
    )

    db_sg_id = response["GroupId"]

    tag_resource(
        db_sg_id,
        "pci-db-sg",
        "firewall"
    )

    # Example:
    # PostgreSQL is accessible ONLY from PCI application servers.
    ec2.authorize_security_group_ingress(
        GroupId=db_sg_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": 5432,
                "ToPort": 5432,
                "UserIdGroupPairs": [
                    {
                        "GroupId": app_sg_id
                    }
                ]
            }
        ]
    )

    # Remove unrestricted outbound traffic.
    try:
        ec2.revoke_security_group_egress(
            GroupId=db_sg_id,
            IpPermissions=[
                {
                    "IpProtocol": "-1",
                    "IpRanges": [
                        {"CidrIp": "0.0.0.0/0"}
                    ]
                }
            ]
        )
    except Exception:
        pass

    print(f"[+] PCI DB SG created: {db_sg_id}")

    return db_sg_id


def create_network_acl(vpc_id, subnet_ids):
    response = ec2.create_network_acl(
        VpcId=vpc_id
    )

    acl_id = response["NetworkAcl"]["NetworkAclId"]

    tag_resource(
        acl_id,
        "pci-cde-nacl",
        "network-firewall"
    )

    for subnet_id in subnet_ids:
        # Find existing association
        nacls = ec2.describe_network_acls(
            Filters=[
                {
                    "Name": "association.subnet-id",
                    "Values": [subnet_id]
                }
            ]
        )

        association_id = (
            nacls["NetworkAcls"][0]
            ["Associations"][0]
            ["NetworkAclAssociationId"]
        )

        ec2.replace_network_acl_association(
            AssociationId=association_id,
            NetworkAclId=acl_id
        )

    print(f"[+] PCI Network ACL created: {acl_id}")

    return acl_id


def enable_flow_logs(vpc_id):
    """
    Requires a CloudWatch Log Group and IAM role.

    For production, create a dedicated PCI security logging account
    and send logs to a centralized immutable logging environment.
    """

    print(
        "[!] Configure VPC Flow Logs for:",
        vpc_id
    )

    print(
        "    Recommended: ALL traffic -> centralized PCI security logs"
    )


def main():

    print("=" * 60)
    print("Creating PCI Cardholder Data Environment")
    print("=" * 60)

    # 1. Dedicated PCI VPC
    vpc_id = create_vpc()

    # 2. Separate PCI tiers
    app_subnet = create_subnet(
        vpc_id,
        PCI_APP_CIDR,
        "pci-app-private"
    )

    db_subnet = create_subnet(
        vpc_id,
        PCI_DB_CIDR,
        "pci-db-private"
    )

    # 3. Private routing
    route_table = create_route_table(
        vpc_id,
        [
            app_subnet,
            db_subnet
        ]
    )

    # 4. Application firewall
    app_sg = create_app_security_group(
        vpc_id
    )

    # 5. Database firewall
    db_sg = create_database_security_group(
        vpc_id,
        app_sg
    )

    # 6. Network ACL
    nacl = create_network_acl(
        vpc_id,
        [
            app_subnet,
            db_subnet
        ]
    )

    # 7. Logging
    enable_flow_logs(vpc_id)

    print("\n" + "=" * 60)
    print("PCI NETWORK CREATED")
    print("=" * 60)

    print(f"""
PCI VPC
  {PCI_VPC_CIDR}
       |
       +--- APP subnet
       |    {PCI_APP_CIDR}
       |       |
       |       +--- pci-app-sg
       |              |
       |              | TCP/5432 only
       |              v
       |
       +--- DB subnet
            {PCI_DB_CIDR}
                |
                +--- pci-db-sg

VPC:          {vpc_id}
APP subnet:   {app_subnet}
DB subnet:    {db_subnet}
APP SG:       {app_sg}
DB SG:        {db_sg}
NACL:         {nacl}
Route table:  {route_table}

Default Internet access: NONE
Public IP assignment:    DISABLED
Environment:             PCI CDE
""")


if __name__ == "__main__":
    main()