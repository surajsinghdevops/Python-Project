from modules.ec2_inventory import get_ec2_inventory


def main():

    print("=" * 60)
    print(" AWS Infrastructure Health Monitor ")
    print("=" * 60)

    instances = get_ec2_inventory()

    if not instances:
        print("No EC2 instances found.")
        return

    for instance in instances:

        print("-" * 60)

        print(f"Name               : {instance['Name']}")
        print(f"Instance ID        : {instance['Instance ID']}")
        print(f"State              : {instance['State']}")
        print(f"Instance Type      : {instance['Instance Type']}")
        print(f"Public IP          : {instance['Public IP']}")
        print(f"Private IP         : {instance['Private IP']}")
        print(f"Availability Zone  : {instance['Availability Zone']}")
        print(f"Launch Time        : {instance['Launch Time']}")

    print("-" * 60)


if __name__ == "__main__":
    main()
