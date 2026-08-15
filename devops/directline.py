import boto3

AWS_REGION = "us-east-1"

# GCP VPN public IP
GCP_VPN_PUBLIC_IP = "34.x.x.x"

# Your GCP VPC CIDR
GCP_CIDR = "10.20.0.0/16"

# AWS VPC CIDR
AWS_VPC_ID = "vpc-xxxxxxxx"

ec2 = boto3.client("ec2", region_name=AWS_REGION)

# -------------------------------------------------
# 1. Create Customer Gateway
# -------------------------------------------------

customer_gateway = ec2.create_customer_gateway(
    Type="ipsec.1",
    PublicIp=GCP_VPN_PUBLIC_IP,
    BgpAsn=65000
)

customer_gateway_id = customer_gateway["CustomerGateway"]["CustomerGatewayId"]

print("Customer Gateway:", customer_gateway_id)

# -------------------------------------------------
# 2. Create Virtual Private Gateway
# -------------------------------------------------

vgw = ec2.create_vpn_gateway(
    Type="ipsec.1",
    AmazonSideAsn=64512
)

vgw_id = vgw["VpnGateway"]["VpnGatewayId"]

print("Virtual Private Gateway:", vgw_id)

# -------------------------------------------------
# 3. Attach VGW to AWS VPC
# -------------------------------------------------

ec2.attach_vpn_gateway(
    VpcId=AWS_VPC_ID,
    VpnGatewayId=vgw_id
)

print("VGW attached to VPC")

# -------------------------------------------------
# 4. Create Site-to-Site VPN
# -------------------------------------------------

vpn = ec2.create_vpn_connection(
    Type="ipsec.1",
    CustomerGatewayId=customer_gateway_id,
    TransitGatewayId=None,
    VpnGatewayId=vgw_id,
    Options={
        "StaticRoutesOnly": True
    }
)

vpn_id = vpn["VpnConnection"]["VpnConnectionId"]

print("VPN Connection:", vpn_id)

# -------------------------------------------------
# 5. Add GCP network
# -------------------------------------------------

ec2.create_vpn_connection_route(
    DestinationCidrBlock=GCP_CIDR,
    VpnConnectionId=vpn_id
)

print("Route added:", GCP_CIDR)

print("\nAWS VPN configuration created successfully.")