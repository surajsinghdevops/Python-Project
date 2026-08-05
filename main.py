from modules.ec2_inventory import get_ec2_inventory

from modules.cloudwatch_metrics import (
    get_cpu_utilization,
    get_network_in,
    get_network_out,
    get_disk_read,
    get_disk_write,
    get_status_check
)

from modules.ebs_details import get_volume_details
from modules.health_checker import cpu_health
from modules.report_generator import (
    generate_csv,
    generate_excel,
    generate_json
)


def main():

    print("=" * 60)
    print("        AWS Infrastructure Health Monitor")
    print("=" * 60)

    instances = get_ec2_inventory()

    if not instances:
        print("No EC2 instances found.")
        return

    report = []

    for instance in instances:

        # -----------------------------
        # CloudWatch Metrics
        # -----------------------------

        cpu = get_cpu_utilization(instance["Instance ID"])
        network_in = get_network_in(instance["Instance ID"])
        network_out = get_network_out(instance["Instance ID"])
        disk_read = get_disk_read(instance["Instance ID"])
        disk_write = get_disk_write(instance["Instance ID"])
        status = get_status_check(instance["Instance ID"])

        # -----------------------------
        # Health Check
        # -----------------------------

        health = cpu_health(cpu)

        # -----------------------------
        # EBS Details
        # -----------------------------

        volumes = get_volume_details(instance["Instance ID"])

        # -----------------------------
        # Display Instance Information
        # -----------------------------

        print("-" * 60)
        print(f"Name               : {instance['Name']}")
        print(f"Instance ID        : {instance['Instance ID']}")
        print(f"State              : {instance['State']}")
        print(f"Instance Type      : {instance['Instance Type']}")
        print(f"Public IP          : {instance['Public IP']}")
        print(f"Private IP         : {instance['Private IP']}")
        print(f"Availability Zone  : {instance['Availability Zone']}")
        print(f"Launch Time        : {instance['Launch Time']}")

        print("\nCloudWatch Metrics")
        print(f"CPU Utilization    : {cpu}%")
        print(f"Network In         : {network_in} Bytes")
        print(f"Network Out        : {network_out} Bytes")
        print(f"Disk Read Bytes    : {disk_read} Bytes")
        print(f"Disk Write Bytes   : {disk_write} Bytes")
        print(f"Status Checks      : {status}")

        print(f"\nHealth Status      : {health}")

        print("\nAttached Volumes")

        for volume in volumes:

            print(f"Volume ID          : {volume['Volume ID']}")
            print(f"Volume Size        : {volume['Size']} GB")
            print(f"Volume Type        : {volume['Type']}")
            print(f"Encrypted          : {volume['Encrypted']}")
            print(f"Volume State       : {volume['State']}")
            print("-" * 30)

        # -----------------------------
        # Store Report Data
        # -----------------------------

        report.append({

            "Name": instance["Name"],
            "Instance ID": instance["Instance ID"],
            "State": instance["State"],
            "Instance Type": instance["Instance Type"],
            "Public IP": instance["Public IP"],
            "Private IP": instance["Private IP"],
            "Availability Zone": instance["Availability Zone"],
            "Launch Time": instance["Launch Time"],

            "CPU Utilization": cpu,
            "Network In": network_in,
            "Network Out": network_out,
            "Disk Read Bytes": disk_read,
            "Disk Write Bytes": disk_write,
            "Status Check": status,

            "Health": health

        })

    # ----------------------------------
    # Generate CSV Report
    # ----------------------------------

    generate_csv(report)

    generate_excel(report)

    generate_json(report)

    # ----------------------------------
    # Infrastructure Summary
    # ----------------------------------

    running = sum(
        1 for item in report
        if item["State"] == "running"
    )

    stopped = sum(
        1 for item in report
        if item["State"] != "running"
    )

    print("\n" + "=" * 60)
    print("Infrastructure Summary")
    print("=" * 60)

    print(f"Total Instances    : {len(report)}")
    print(f"Running Instances  : {running}")
    print(f"Stopped Instances  : {stopped}")

    print("=" * 60)


if __name__ == "__main__":
    main()
