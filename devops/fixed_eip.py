import boto3
import time

# ==========================
# Configuration
# ==========================

REGION = "us-east-1"

VPC_CIDR = "10.0.0.0/16"
PUBLIC_SUBNET_CIDR = "10.0.1.0/24"
PRIVATE_SUBNET_CIDR = "10.0.2.0/24"

vpc_name = "fixed-egress-vpc"


# ==========================
# AWS clients
# ==========================

ec2 = boto3.client("ec2", region_name=REGION)


# ==========================
# 1. Create VPC
# ==========================

print("Creating VPC...")

vpc = ec2.create_vpc(
    CidrBlock=VPC_CIDR,
    TagSpecifications=[
        {
            "ResourceType": "vpc",
            "Tags": [
                {"Key": "Name", "Value": vpc_name}
            ]
        }
    ]
)

vpc_id = vpc["Vpc"]["VpcId"]

# Enable DNS
ec2.modify_vpc_attribute(
    VpcId=vpc_id,
    EnableDnsSupport={"Value": True}
)

ec2.modify_vpc_attribute(
    VpcId=vpc_id,
    EnableDnsHostnames={"Value": True}
)

print(f"VPC created: {vpc_id}")


# ==========================
# 2. Get Availability Zone
# ==========================

azs = ec2.describe_availability_zones(
    Filters=[
        {
            "Name": "state",
            "Values": ["available"]
        }
    ]
)

AZ = azs["AvailabilityZones"][0]["ZoneName"]

print(f"Using Availability Zone: {AZ}")


# ==========================
# 3. Create Public Subnet
# ==========================

print("Creating public subnet...")

public_subnet = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock=PUBLIC_SUBNET_CIDR,
    AvailabilityZone=AZ,
    TagSpecifications=[
        {
            "ResourceType": "subnet",
            "Tags": [
                {"Key": "Name", "Value": "public-subnet"}
            ]
        }
    ]
)

public_subnet_id = public_subnet["Subnet"]["SubnetId"]

print(f"Public subnet: {public_subnet_id}")


# ==========================
# 4. Create Private Subnet
# ==========================

print("Creating private subnet...")

private_subnet = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock=PRIVATE_SUBNET_CIDR,
    AvailabilityZone=AZ,
    TagSpecifications=[
        {
            "ResourceType": "subnet",
            "Tags": [
                {"Key": "Name", "Value": "private-subnet"}
            ]
        }
    ]
)

private_subnet_id = private_subnet["Subnet"]["SubnetId"]

print(f"Private subnet: {private_subnet_id}")


# ==========================
# 5. Create Internet Gateway
# ==========================

print("Creating Internet Gateway...")

igw = ec2.create_internet_gateway(
    TagSpecifications=[
        {
            "ResourceType": "internet-gateway",
            "Tags": [
                {"Key": "Name", "Value": "fixed-egress-igw"}
            ]
        }
    ]
)

igw_id = igw["InternetGateway"]["InternetGatewayId"]

ec2.attach_internet_gateway(
    VpcId=vpc_id,
    InternetGatewayId=igw_id
)

print(f"Internet Gateway: {igw_id}")


# ==========================
# 6. Create Public Route Table
# ==========================

print("Creating public route table...")

public_rt = ec2.create_route_table(
    VpcId=vpc_id,
    TagSpecifications=[
        {
            "ResourceType": "route-table",
            "Tags": [
                {"Key": "Name", "Value": "public-route-table"}
            ]
        }
    ]
)

public_rt_id = public_rt["RouteTable"]["RouteTableId"]

ec2.create_route(
    RouteTableId=public_rt_id,
    DestinationCidrBlock="0.0.0.0/0",
    GatewayId=igw_id
)

ec2.associate_route_table(
    RouteTableId=public_rt_id,
    SubnetId=public_subnet_id
)


# ==========================
# 7. Allocate Elastic IP
# ==========================

print("Allocating Elastic IP...")

eip = ec2.allocate_address(
    Domain="vpc"
)

allocation_id = eip["AllocationId"]
elastic_ip = eip["PublicIp"]

print(f"Elastic IP: {elastic_ip}")


# ==========================
# 8. Create NAT Gateway
# ==========================

print("Creating NAT Gateway...")

nat = ec2.create_nat_gateway(
    SubnetId=public_subnet_id,
    AllocationId=allocation_id,
    TagSpecifications=[
        {
            "ResourceType": "natgateway",
            "Tags": [
                {"Key": "Name", "Value": "fixed-egress-nat"}
            ]
        }
    ]
)

nat_gateway_id = nat["NatGateway"]["NatGatewayId"]

print(f"NAT Gateway: {nat_gateway_id}")

print("Waiting for NAT Gateway...")

waiter = ec2.get_waiter("nat_gateway_available")

waiter.wait(
    NatGatewayIds=[nat_gateway_id]
)

print("NAT Gateway is available.")


# ==========================
# 9. Create Private Route Table
# ==========================

print("Creating private route table...")

private_rt = ec2.create_route_table(
    VpcId=vpc_id,
    TagSpecifications=[
        {
            "ResourceType": "route-table",
            "Tags": [
                {"Key": "Name", "Value": "private-route-table"}
            ]
        }
    ]
)

private_rt_id = private_rt["RouteTable"]["RouteTableId"]


# ==========================
# 10. Route private traffic
# ==========================

ec2.create_route(
    RouteTableId=private_rt_id,
    DestinationCidrBlock="0.0.0.0/0",
    NatGatewayId=nat_gateway_id
)

ec2.associate_route_table(
    RouteTableId=private_rt_id,
    SubnetId=private_subnet_id
)


# ==========================
# Finished
# ==========================

print("\n======================================")
print("Fixed Egress IP configuration complete")
print("======================================")

print(f"VPC ID:             {vpc_id}")
print(f"Public Subnet:      {public_subnet_id}")
print(f"Private Subnet:     {private_subnet_id}")
print(f"Internet Gateway:   {igw_id}")
print(f"NAT Gateway:        {nat_gateway_id}")
print(f"Elastic IP:         {elastic_ip}")

print("\nOutbound Internet IP:")
print(elastic_ip)

print("\nPrivate resources should use:")
print("Private Subnet -> NAT Gateway -> Elastic IP")