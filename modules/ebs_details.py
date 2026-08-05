import boto3

from config.config import AWS_REGION

ec2 = boto3.client(
    "ec2",
    region_name=AWS_REGION
)


def get_volume_details(instance_id):

    response = ec2.describe_instances(
        InstanceIds=[instance_id]
    )

    volumes = []

    for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            if "BlockDeviceMappings" not in instance:
                continue

            for block in instance["BlockDeviceMappings"]:

                volume_id = block["Ebs"]["VolumeId"]

                volume = ec2.describe_volumes(
                    VolumeIds=[volume_id]
                )["Volumes"][0]

                volumes.append({

                    "Volume ID": volume["VolumeId"],

                    "Size": volume["Size"],

                    "Type": volume["VolumeType"],

                    "Encrypted": volume["Encrypted"],

                    "State": volume["State"]

                })

    return volumes
