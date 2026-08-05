import boto3

from datetime import datetime, timedelta, timezone

from config.config import AWS_REGION
from config.config import METRIC_PERIOD

cloudwatch = boto3.client(
    "cloudwatch",
    region_name=AWS_REGION
)


def get_metric(instance_id, metric_name):

    end_time = datetime.now(timezone.utc)

    start_time = end_time - timedelta(minutes=10)

    response = cloudwatch.get_metric_statistics(

        Namespace="AWS/EC2",

        MetricName=metric_name,

        Dimensions=[
            {
                "Name": "InstanceId",
                "Value": instance_id
            }
        ],

        StartTime=start_time,

        EndTime=end_time,

        Period=METRIC_PERIOD,

        Statistics=["Average"]

    )

    datapoints = response["Datapoints"]

    if not datapoints:
        return 0

    latest = max(
        datapoints,
        key=lambda x: x["Timestamp"]
    )

    return round(
        latest["Average"],
        2
    )


def get_cpu_utilization(instance_id):
    return get_metric(
        instance_id,
        "CPUUtilization"
    )


def get_network_in(instance_id):
    return get_metric(
        instance_id,
        "NetworkIn"
    )


def get_network_out(instance_id):
    return get_metric(
        instance_id,
        "NetworkOut"
    )


def get_disk_read(instance_id):
    return get_metric(
        instance_id,
        "DiskReadBytes"
    )


def get_disk_write(instance_id):
    return get_metric(
        instance_id,
        "DiskWriteBytes"
    )


def get_status_check(instance_id):
    return get_metric(
        instance_id,
        "StatusCheckFailed"
    )
