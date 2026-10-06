import boto3
from botocore.exceptions import ClientError

REGION = "us-east-1"

VPC_A_ID = "vpc-0123456789abcdef0"
VPC_B_ID = "vpc-0fedcba9876543210"

VPC_A_CIDR = "10.10.0.0/16"
VPC_B_CIDR = "10.20.0.0/16"

# Route tables that should use the tunnel/peering connection
VPC_A_ROUTE_TABLE = "rtb-0123456789abcdef0"
VPC_B_ROUTE_TABLE = "rtb-0fedcba9876543210"

ec2 = boto3.client("ec2", region_name=REGION)


def create_vpc_peering():
    try:
        response = ec2.create_vpc_peering_connection(
            VpcId=VPC_A_ID,
            PeerVpcId=VPC_B_ID
        )

        peering_id = response["VpcPeeringConnection"]["VpcPeeringConnectionId"]

        print(f"Created VPC peering connection: {peering_id}")

        # Wait until AWS recognizes the connection
        waiter = ec2.get_waiter("vpc_peering_connection_exists")
        waiter.wait(
            VpcPeeringConnectionIds=[peering_id]
        )

        return peering_id

    except ClientError as error:
        print(f"Error creating peering connection: {error}")
        raise


def accept_peering(peering_id):
    try:
        ec2.accept_vpc_peering_connection(
            VpcPeeringConnectionId=peering_id
        )

        print(f"Accepted peering connection: {peering_id}")

    except ClientError as error:
        print(f"Error accepting peering connection: {error}")
        raise


def create_route(route_table_id, destination_cidr, peering_id):
    try:
        ec2.create_route(
            RouteTableId=route_table_id,
            DestinationCidrBlock=destination_cidr,
            VpcPeeringConnectionId=peering_id
        )

        print(
            f"Route added: {route_table_id} "
            f"-> {destination_cidr}"
        )

    except ClientError as error:

        # Ignore route if it already exists
        if "RouteAlreadyExists" in str(error):
            print(
                f"Route already exists: "
                f"{route_table_id} -> {destination_cidr}"
            )
        else:
            raise


def main():

    print("Creating private connection between VPCs...")

    peering_id = create_vpc_peering()

    accept_peering(peering_id)

    print("Configuring VPC A route...")

    create_route(
        VPC_A_ROUTE_TABLE,
        VPC_B_CIDR,
        peering_id
    )

    print("Configuring VPC B route...")

    create_route(
        VPC_B_ROUTE_TABLE,
        VPC_A_CIDR,
        peering_id
    )

    print("\nConfiguration completed.")
    print(f"VPC A: {VPC_A_CIDR}")
    print(f"VPC B: {VPC_B_CIDR}")
    print(f"Peering: {peering_id}")


if __name__ == "__main__":
    main()