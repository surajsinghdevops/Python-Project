
import boto3
from datetime import datetime, timedelta, timezone

from config.config import AWS_REGION


cloudwatch = boto3.client(
    "cloudwatch",
    region_name=AWS_REGION
)


def get_cpu_utilization(instance_id):

    end_time = datetime.now(timezone.utc)

    start_time = end_time - timedelta(minutes=10)

    response = cloudwatch.get_metric_statistics(

        Namespace="AWS/EC2",

        MetricName="CPUUtilization",

        Dimensions=[
            {
                "Name": "InstanceId",
                "Value": instance_id
            }
        ],

        StartTime=start_time,

        EndTime=end_time,

        Period=300,

        Statistics=["Average"]

    )

    datapoints = response["Datapoints"]

    if not datapoints:
        return 0

    latest = sorted(
        datapoints,
        key=lambda x: x["Timestamp"]
    )[-1]

    return round(latest["Average"], 2)
