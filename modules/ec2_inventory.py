import boto3
from config.config import AWS_REGION


def get_ec2_inventory():
    """
    Fetch EC2 instance inventory from AWS.
    """

    ec2 = boto3.client("ec2", region_name=AWS_REGION)

    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            name = "N/A"

            if "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Name":
                        name = tag["Value"]

            instances.append({

                "Name": name,

                "Instance ID": instance["InstanceId"],

                "State": instance["State"]["Name"],

                "Instance Type": instance["InstanceType"],

                "Public IP": instance.get("PublicIpAddress", "N/A"),

                "Private IP": instance.get("PrivateIpAddress", "N/A"),

                "Availability Zone": instance["Placement"]["AvailabilityZone"],

                "Launch Time": str(instance["LaunchTime"])

            })

    return instances
