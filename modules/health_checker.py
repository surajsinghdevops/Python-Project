def cpu_health(cpu):

    if cpu < 50:
        return "Healthy"

    elif cpu < 80:
        return "Warning"

    else:
        return "Critical"
