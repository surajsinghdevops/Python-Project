import pandas as pd
import json
import os


REPORT_FOLDER = "reports"


def create_report_folder():

    if not os.path.exists(REPORT_FOLDER):
        os.makedirs(REPORT_FOLDER)


def generate_csv(data):

    create_report_folder()

    df = pd.DataFrame(data)

    csv_path = os.path.join(
        REPORT_FOLDER,
        "infrastructure_report.csv"
    )

    df.to_csv(
        csv_path,
        index=False
    )

    print("✓ CSV Report Generated")


def generate_excel(data):

    create_report_folder()

    df = pd.DataFrame(data)

    excel_path = os.path.join(
        REPORT_FOLDER,
        "infrastructure_report.xlsx"
    )

    df.to_excel(
        excel_path,
        index=False
    )

    print("✓ Excel Report Generated")


def generate_json(data):

    create_report_folder()

    json_path = os.path.join(
        REPORT_FOLDER,
        "infrastructure_report.json"
    )

    with open(
        json_path,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            default=str
        )

    print("✓ JSON Report Generated")
