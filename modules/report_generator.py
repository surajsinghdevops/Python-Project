import pandas as pd


def generate_csv(data):

    df = pd.DataFrame(data)

    df.to_csv(
        "reports/infrastructure_report.csv",
        index=False
    )

    print("\nCSV Report Generated Successfully")
