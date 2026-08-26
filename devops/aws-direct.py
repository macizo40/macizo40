import boto3
import time
import secrets
import sys
from botocore.exceptions import ClientError, NoCredentialsError


# ==========================================================
# CONFIGURATION
# ==========================================================

AWS_REGION = "us-east-1"

# Direct Connect physical connection
CONNECTION_NAME = "onprem-datacenter-dx"
DX_LOCATION = "EqDC2"       # Example only - replace with your DX location
BANDWIDTH = "1Gbps"

# Private Virtual Interface
VIF_NAME = "onprem-private-vif"
VLAN_ID = 101

# ASN of your on-premises router
CUSTOMER_ASN = 65000

# Point-to-point BGP IPs
CUSTOMER_ROUTER_IP = "169.254.100.2/30"
AWS_ROUTER_IP = "169.254.100.1/30"

# Existing AWS Virtual Private Gateway
#
# Example:
# vgw-0123456789abcdef0
VIRTUAL_GATEWAY_ID = "vgw-0123456789abcdef0"


# ==========================================================
# AWS CLIENT
# ==========================================================

def get_direct_connect_client():

    try:
        client = boto3.client(
            "directconnect",
            region_name=AWS_REGION
        )

        return client

    except NoCredentialsError:
        print("AWS credentials were not found.")
        sys.exit(1)


# ==========================================================
# SHOW AVAILABLE DIRECT CONNECT LOCATIONS
# ==========================================================

def show_direct_connect_locations(client):

    print("\nAvailable AWS Direct Connect locations:\n")

    response = client.describe_locations()

    for location in response["locations"]:

        print(
            f"{location['locationCode']:<15} "
            f"{location['locationName']}"
        )


# ==========================================================
# CREATE DIRECT CONNECT CONNECTION
# ==========================================================

def create_direct_connect_connection(client):

    print("\nCreating AWS Direct Connect connection...")

    try:

        response = client.create_connection(

            location=DX_LOCATION,

            bandwidth=BANDWIDTH,

            connectionName=CONNECTION_NAME,

            tags=[
                {
                    "key": "Environment",
                    "value": "Production"
                },
                {
                    "key": "Connection",
                    "value": "OnPrem"
                },
                {
                    "key": "ManagedBy",
                    "value": "Python"
                }
            ]
        )

        connection_id = response["connectionId"]

        print("\nDirect Connect request created.")
        print(f"Connection ID: {connection_id}")
        print(f"State: {response['connectionState']}")

        return connection_id

    except ClientError as error:

        print(
            "Unable to create Direct Connect connection:"
        )

        print(error)

        sys.exit(1)


# ==========================================================
# CHECK CONNECTION STATUS
# ==========================================================

def get_connection_status(client, connection_id):

    response = client.describe_connections(
        connectionId=connection_id
    )

    connections = response.get("connections", [])

    if not connections:
        return None

    return connections[0]["connectionState"]


# ==========================================================
# WAIT FOR DIRECT CONNECT
# ==========================================================

def wait_for_connection(client, connection_id):

    print("\nWaiting for Direct Connect connection...")

    while True:

        status = get_connection_status(
            client,
            connection_id
        )

        print(f"Connection status: {status}")

        if status == "available":

            print(
                "\nDirect Connect connection is available."
            )

            return

        if status in [
            "deleted",
            "rejected",
            "unknown"
        ]:

            raise RuntimeError(
                f"Connection entered state: {status}"
            )

        print(
            "Physical/provider provisioning may still "
            "be required."
        )

        time.sleep(60)


# ==========================================================
# CREATE PRIVATE VIRTUAL INTERFACE
# ==========================================================

def create_private_virtual_interface(
        client,
        connection_id
):

    print("\nCreating private virtual interface...")

    # Generate BGP authentication key
    bgp_auth_key = secrets.token_urlsafe(32)

    try:

        response = client.create_private_virtual_interface(

            connectionId=connection_id,

            newPrivateVirtualInterface={

                "virtualInterfaceName":
                    VIF_NAME,

                "vlan":
                    VLAN_ID,

                "asn":
                    CUSTOMER_ASN,

                "authKey":
                    bgp_auth_key,

                "amazonAddress":
                    AWS_ROUTER_IP,

                "customerAddress":
                    CUSTOMER_ROUTER_IP,

                "addressFamily":
                    "ipv4",

                "virtualGatewayId":
                    VIRTUAL_GATEWAY_ID,

                "mtu":
                    1500,

                "tags": [
                    {
                        "key": "Environment",
                        "value": "Production"
                    },
                    {
                        "key": "Connection",
                        "value": "OnPrem"
                    }
                ]
            }
        )

        print("\nPrivate VIF created.")

        print(
            "Virtual Interface ID:",
            response["virtualInterfaceId"]
        )

        print(
            "Virtual Interface State:",
            response["virtualInterfaceState"]
        )

        print(
            "\nIMPORTANT: Configure the generated "
            "BGP authentication key securely on "
            "your on-premises router."
        )

        return response

    except ClientError as error:

        print(
            "Unable to create private virtual interface:"
        )

        print(error)

        sys.exit(1)


# ==========================================================
# DISPLAY VIF INFORMATION
# ==========================================================

def show_virtual_interface(client, vif_id):

    response = client.describe_virtual_interfaces(
        virtualInterfaceId=vif_id
    )

    for vif in response["virtualInterfaces"]:

        print("\n--------------------------------")
        print("Direct Connect VIF")
        print("--------------------------------")

        print(
            "VIF ID:",
            vif["virtualInterfaceId"]
        )

        print(
            "State:",
            vif["virtualInterfaceState"]
        )

        print(
            "VLAN:",
            vif["vlan"]
        )

        print(
            "Customer IP:",
            vif.get("customerAddress")
        )

        print(
            "AWS IP:",
            vif.get("amazonAddress")
        )

        print(
            "Customer ASN:",
            vif.get("asn")
        )

        print(
            "AWS ASN:",
            vif.get("amazonSideAsn")
        )


# ==========================================================
# MAIN
# ==========================================================

def main():

    print(
        "\n======================================"
    )

    print(
        " AWS Direct Connect Provisioning"
    )

    print(
        "======================================"
    )

    client = get_direct_connect_client()

    # Optional:
    # Uncomment this first to discover the correct
    # DX_LOCATION for your area.
    #
    # show_direct_connect_locations(client)

    connection_id = create_direct_connect_connection(
        client
    )

    print(
        "\nAWS connection request created."
    )

    print(
        "\nNOTE:"
        "\nThe physical Direct Connect circuit must now"
        "\nbe provisioned by AWS and/or your Direct"
        "\nConnect connectivity provider."
    )

    # Normally you should run VIF creation only after
    # the physical connection becomes available.
    #
    # wait_for_connection(client, connection_id)

    # vif = create_private_virtual_interface(
    #     client,
    #     connection_id
    # )
    #
    # show_virtual_interface(
    #     client,
    #     vif["virtualInterfaceId"]
    # )


if __name__ == "__main__":
    main()