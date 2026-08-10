#!/usr/bin/env python3

import boto3
import time
from botocore.exceptions import ClientError

# ============================================================
# Configuration
# ============================================================

REGION = "us-east-1"

VPC_CIDR = "10.50.0.0/16"

PUBLIC_SUBNETS = [
    {
        "name": "data-sync-public-a",
        "cidr": "10.50.1.0/24",
        "az": f"{REGION}a"
    },
    {
        "name": "data-sync-public-b",
        "cidr": "10.50.2.0/24",
        "az": f"{REGION}b"
    }
]

PRIVATE_SUBNETS = [
    {
        "name": "data-sync-private-a",
        "cidr": "10.50.11.0/24",
        "az": f"{REGION}a"
    },
    {
        "name": "data-sync-private-b",
        "cidr": "10.50.12.0/24",
        "az": f"{REGION}b"
    }
]

VPC_NAME = "data-sync-vpc"


# ============================================================
# AWS clients
# ============================================================

ec2 = boto3.client("ec2", region_name=REGION)


# ============================================================
# Helper functions
# ============================================================

def create_tags(resource_id, name):
    ec2.create_tags(
        Resources=[resource_id],
        Tags=[
            {
                "Key": "Name",
                "Value": name
            },
            {
                "Key": "Project",
                "Value": "DataSync"
            },
            {
                "Key": "Environment",
                "Value": "dedicated"
            },
            {
                "Key": "ManagedBy",
                "Value": "Python"
            }
        ]
    )


def create_vpc():
    print("Creating VPC...")

    response = ec2.create_vpc(
        CidrBlock=VPC_CIDR,
        TagSpecifications=[
            {
                "ResourceType": "vpc",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": VPC_NAME
                    },
                    {
                        "Key": "Project",
                        "Value": "DataSync"
                    }
                ]
            }
        ]
    )

    vpc_id = response["Vpc"]["VpcId"]

    ec2.modify_vpc_attribute(
        VpcId=vpc_id,
        EnableDnsSupport={"Value": True}
    )

    ec2.modify_vpc_attribute(
        VpcId=vpc_id,
        EnableDnsHostnames={"Value": True}
    )

    print(f"VPC created: {vpc_id}")

    return vpc_id


def create_subnets(vpc_id, subnet_config):
    subnet_ids = []

    for subnet in subnet_config:

        print(
            f"Creating subnet "
            f"{subnet['name']} "
            f"{subnet['cidr']}..."
        )

        response = ec2.create_subnet(
            VpcId=vpc_id,
            CidrBlock=subnet["cidr"],
            AvailabilityZone=subnet["az"],
            TagSpecifications=[
                {
                    "ResourceType": "subnet",
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": subnet["name"]
                        },
                        {
                            "Key": "Project",
                            "Value": "DataSync"
                        }
                    ]
                }
            ]
        )

        subnet_id = response["Subnet"]["SubnetId"]

        subnet_ids.append(subnet_id)

        print(f"Created: {subnet_id}")

    return subnet_ids


def create_internet_gateway(vpc_id):

    print("Creating Internet Gateway...")

    response = ec2.create_internet_gateway()

    igw_id = response["InternetGateway"]["InternetGatewayId"]

    create_tags(
        igw_id,
        "data-sync-igw"
    )

    ec2.attach_internet_gateway(
        InternetGatewayId=igw_id,
        VpcId=vpc_id
    )

    print(f"Internet Gateway: {igw_id}")

    return igw_id


def create_route_table(vpc_id, name):

    response = ec2.create_route_table(
        VpcId=vpc_id
    )

    route_table_id = response["RouteTable"]["RouteTableId"]

    create_tags(
        route_table_id,
        name
    )

    return route_table_id


def associate_route_table(route_table_id, subnet_id):

    ec2.associate_route_table(
        RouteTableId=route_table_id,
        SubnetId=subnet_id
    )


def create_public_route_table(vpc_id, igw_id, public_subnets):

    print("Creating public route table...")

    route_table_id = create_route_table(
        vpc_id,
        "data-sync-public-rt"
    )

    ec2.create_route(
        RouteTableId=route_table_id,
        DestinationCidrBlock="0.0.0.0/0",
        GatewayId=igw_id
    )

    for subnet_id in public_subnets:

        associate_route_table(
            route_table_id,
            subnet_id
        )

    return route_table_id


def create_nat_gateway(public_subnet_id, name):

    print(
        f"Creating NAT Gateway in {public_subnet_id}..."
    )

    allocation = ec2.allocate_address(
        Domain="vpc"
    )

    allocation_id = allocation["AllocationId"]
    public_ip = allocation["PublicIp"]

    nat = ec2.create_nat_gateway(
        SubnetId=public_subnet_id,
        AllocationId=allocation_id,
        TagSpecifications=[
            {
                "ResourceType": "natgateway",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": name
                    },
                    {
                        "Key": "Project",
                        "Value": "DataSync"
                    }
                ]
            }
        ]
    )

    nat_id = nat["NatGateway"]["NatGatewayId"]

    print(
        f"NAT Gateway created: {nat_id} "
        f"({public_ip})"
    )

    print("Waiting for NAT Gateway...")

    waiter = ec2.get_waiter(
        "nat_gateway_available"
    )

    waiter.wait(
        NatGatewayIds=[nat_id]
    )

    print(
        f"NAT Gateway available: {nat_id}"
    )

    return nat_id


def create_private_route_table(
    vpc_id,
    private_subnet_id,
    nat_gateway_id,
    name
):

    route_table_id = create_route_table(
        vpc_id,
        name
    )

    ec2.create_route(
        RouteTableId=route_table_id,
        DestinationCidrBlock="0.0.0.0/0",
        NatGatewayId=nat_gateway_id
    )

    associate_route_table(
        route_table_id,
        private_subnet_id
    )

    return route_table_id


def create_security_group(vpc_id):

    print("Creating security group...")

    response = ec2.create_security_group(
        GroupName="data-sync-sg",
        Description="Security group for Data Sync workloads",
        VpcId=vpc_id
    )

    sg_id = response["GroupId"]

    create_tags(
        sg_id,
        "data-sync-sg"
    )

    # --------------------------------------------------------
    # IMPORTANT:
    # Do not open the security group to the Internet.
    #
    # Add specific source CIDRs/security groups depending
    # on the systems being synchronized.
    # --------------------------------------------------------

    print(f"Security Group: {sg_id}")

    return sg_id


def create_s3_endpoint(vpc_id, route_table_ids):

    print("Creating S3 Gateway Endpoint...")

    response = ec2.create_vpc_endpoint(
        VpcId=vpc_id,
        ServiceName=f"com.amazonaws.{REGION}.s3",
        VpcEndpointType="Gateway",
        RouteTableIds=route_table_ids
    )

    endpoint_id = response["VpcEndpoint"]["VpcEndpointId"]

    create_tags(
        endpoint_id,
        "data-sync-s3-endpoint"
    )

    print(f"S3 Endpoint: {endpoint_id}")

    return endpoint_id


# ============================================================
# Main
# ============================================================

def main():

    print("=" * 60)
    print("AWS DATA SYNC VPC CREATION")
    print("=" * 60)

    # --------------------------------------------------------
    # 1. VPC
    # --------------------------------------------------------

    vpc_id = create_vpc()

    # --------------------------------------------------------
    # 2. Subnets
    # --------------------------------------------------------

    public_subnets = create_subnets(
        vpc_id,
        PUBLIC_SUBNETS
    )

    private_subnets = create_subnets(
        vpc_id,
        PRIVATE_SUBNETS
    )

    # --------------------------------------------------------
    # 3. Internet Gateway
    # --------------------------------------------------------

    igw_id = create_internet_gateway(
        vpc_id
    )

    # --------------------------------------------------------
    # 4. Public Route Table
    # --------------------------------------------------------

    create_public_route_table(
        vpc_id,
        igw_id,
        public_subnets
    )

    # --------------------------------------------------------
    # 5. NAT Gateways
    # --------------------------------------------------------

    nat_gateways = []

    for index, subnet_id in enumerate(public_subnets):

        nat_id = create_nat_gateway(
            subnet_id,
            f"data-sync-nat-{index + 1}"
        )

        nat_gateways.append(nat_id)

    # --------------------------------------------------------
    # 6. Private Route Tables
    # --------------------------------------------------------

    private_route_tables = []

    for index, subnet_id in enumerate(private_subnets):

        route_table_id = create_private_route_table(
            vpc_id,
            subnet_id,
            nat_gateways[index],
            f"data-sync-private-rt-{index + 1}"
        )

        private_route_tables.append(
            route_table_id
        )

    # --------------------------------------------------------
    # 7. Security Group
    # --------------------------------------------------------

    sg_id = create_security_group(
        vpc_id
    )

    # --------------------------------------------------------
    # 8. S3 VPC Endpoint
    # --------------------------------------------------------

    s3_endpoint_id = create_s3_endpoint(
        vpc_id,
        private_route_tables
    )

    # --------------------------------------------------------
    # Output
    # --------------------------------------------------------

    print()
    print("=" * 60)
    print("DATA SYNC VPC CREATED SUCCESSFULLY")
    print("=" * 60)

    print(f"VPC ID:                 {vpc_id}")
    print(f"VPC CIDR:               {VPC_CIDR}")
    print(f"Internet Gateway:       {igw_id}")
    print(f"Public Subnets:         {public_subnets}")
    print(f"Private Subnets:        {private_subnets}")
    print(f"NAT Gateways:            {nat_gateways}")
    print(f"Private Route Tables:   {private_route_tables}")
    print(f"Security Group:         {sg_id}")
    print(f"S3 Endpoint:            {s3_endpoint_id}")

    print()
    print("Data Sync VPC is ready.")


if __name__ == "__main__":
    main()