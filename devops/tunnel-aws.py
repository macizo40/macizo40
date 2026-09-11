import boto3
import sys

# =========================
# CONFIGURATION
# =========================
AWS_REGION = "us-east-1"

VPC_ID = "vpc-xxxxxxxxxxxxxxxxx"

# Public IP of your on-prem / private cloud firewall or router
CUSTOMER_GATEWAY_PUBLIC_IP = "203.0.113.10"

# Use your real ASN if you already have one.
# AWS commonly uses private ASN ranges as well.
BGP_ASN = 65000

ec2 = boto3.client("ec2", region_name=AWS_REGION)


def create_customer_gateway():
    print("Creating Customer Gateway...")

    response = ec2.create_customer_gateway(
        BgpAsn=BGP_ASN,
        PublicIp=CUSTOMER_GATEWAY_PUBLIC_IP,
        Type="ipsec.1",
        TagSpecifications=[
            {
                "ResourceType": "customer-gateway",
                "Tags": [
                    {"Key": "Name", "Value": "PrivateCloud-CGW"}
                ],
            }
        ],
    )

    cgw_id = response["CustomerGateway"]["CustomerGatewayId"]

    print(f"Customer Gateway created: {cgw_id}")

    return cgw_id


def create_virtual_private_gateway():
    print("Creating Virtual Private Gateway...")

    response = ec2.create_vpn_gateway(
        Type="ipsec.1",
        AmazonSideAsn=64512,
        TagSpecifications=[
            {
                "ResourceType": "vpn-gateway",
                "Tags": [
                    {"Key": "Name", "Value": "PrivateCloud-VGW"}
                ],
            }
        ],
    )

    vgw_id = response["VpnGateway"]["VpnGatewayId"]

    print(f"Virtual Private Gateway created: {vgw_id}")

    return vgw_id


def attach_vpn_gateway(vgw_id):
    print(f"Attaching {vgw_id} to VPC {VPC_ID}...")

    ec2.attach_vpn_gateway(
        VpnGatewayId=vgw_id,
        VpcId=VPC_ID,
    )

    print("VGW attached to VPC.")


def create_vpn_connection(cgw_id, vgw_id):
    print("Creating VPN connection...")

    response = ec2.create_vpn_connection(
        Type="ipsec.1",
        CustomerGatewayId=cgw_id,
        VpnGatewayId=vgw_id,
        Options={
            "StaticRoutesOnly": False,
            "TunnelOptions": [
                {
                    "DPDTimeoutAction": "restart",
                    "StartupAction": "start",
                },
                {
                    "DPDTimeoutAction": "restart",
                    "StartupAction": "start",
                },
            ],
        },
        TagSpecifications=[
            {
                "ResourceType": "vpn-connection",
                "Tags": [
                    {"Key": "Name", "Value": "PrivateCloud-to-AWS"}
                ],
            }
        ],
    )

    vpn_id = response["VpnConnection"]["VpnConnectionId"]

    print(f"VPN created: {vpn_id}")

    return vpn_id


def enable_route_propagation(vgw_id):
    print("Checking VPC route tables...")

    route_tables = ec2.describe_route_tables(
        Filters=[
            {
                "Name": "vpc-id",
                "Values": [VPC_ID],
            }
        ]
    )

    for rt in route_tables["RouteTables"]:
        route_table_id = rt["RouteTableId"]

        print(
            f"Enabling VPN route propagation on "
            f"{route_table_id}"
        )

        try:
            ec2.enable_vgw_route_propagation(
                GatewayId=vgw_id,
                RouteTableId=route_table_id,
            )
        except Exception as exc:
            print(
                f"Could not enable propagation on "
                f"{route_table_id}: {exc}"
            )


def main():
    try:
        cgw_id = create_customer_gateway()

        vgw_id = create_virtual_private_gateway()

        attach_vpn_gateway(vgw_id)

        vpn_id = create_vpn_connection(
            cgw_id,
            vgw_id,
        )

        enable_route_propagation(vgw_id)

        print("\n==============================")
        print("VPN resources created")
        print("==============================")

        print(f"Customer Gateway: {cgw_id}")
        print(f"Virtual Private Gateway: {vgw_id}")
        print(f"VPN Connection: {vpn_id}")

        print("\nNext steps:")
        print(
            "1. Download the VPN configuration from AWS."
        )
        print(
            "2. Configure both IPsec tunnels on your "
            "private-cloud firewall/router."
        )
        print(
            "3. Configure BGP peers if using dynamic routing."
        )
        print(
            "4. Verify AWS and private-cloud routes."
        )
        print(
            "5. Validate Security Groups, NACLs and firewalls."
        )

    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()