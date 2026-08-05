from modules.ec2_inventory import get_ec2_inventory
from modules.cloudwatch_metrics import get_cpu_utilization
from modules.ebs_details import get_volume_details
from modules.health_checker import cpu_health
from modules.report_generator import generate_csv


def main():

    print("=" * 60)
    print(" AWS Infrastructure Health Monitor ")
    print("=" * 60)

    instances = get_ec2_inventory()

    if not instances:
        print("No EC2 instances found.")
        return

    report = []

    for instance in instances:

        cpu = get_cpu_utilization(instance["Instance ID"])
        health = cpu_health(cpu)
        volumes = get_volume_details(instance["Instance ID"])

        print("-" * 60)
        print(f"Name               : {instance['Name']}")
        print(f"Instance ID        : {instance['Instance ID']}")
        print(f"State              : {instance['State']}")
        print(f"CPU Utilization    : {cpu}%")
        print(f"Health Status      : {health}")
        print(f"Instance Type      : {instance['Instance Type']}")
        print(f"Public IP          : {instance['Public IP']}")
        print(f"Private IP         : {instance['Private IP']}")
        print(f"Availability Zone  : {instance['Availability Zone']}")
        print(f"Launch Time        : {instance['Launch Time']}")

        print("\nAttached Volumes")

        for volume in volumes:
            print(f"Volume ID          : {volume['Volume ID']}")
            print(f"Volume Size        : {volume['Size']} GB")
            print(f"Volume Type        : {volume['Type']}")
            print(f"Encrypted          : {volume['Encrypted']}")
            print(f"State              : {volume['State']}")
            print()

        report.append({
            "Name": instance["Name"],
            "Instance ID": instance["Instance ID"],
            "State": instance["State"],
            "CPU": cpu,
            "Health": health
        })

    print("-" * 60)

    generate_csv(report)

    running = sum(1 for item in report if item["State"] == "running")
    stopped = sum(1 for item in report if item["State"] != "running")

    print("\n" + "=" * 60)
    print("Infrastructure Summary")
    print("=" * 60)
    print(f"Running Instances : {running}")
    print(f"Stopped Instances : {stopped}")
    print("=" * 60)


if __name__ == "__main__":
    main()
