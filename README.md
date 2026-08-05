# 🚀 AWS Infrastructure Health Monitor using Python & boto3

## 📌 Project Overview

AWS Infrastructure Health Monitor is a Python-based automation project that collects infrastructure information from AWS, monitors EC2 instance health using CloudWatch metrics, gathers EBS volume details, generates reports in multiple formats, and uploads those reports to Amazon S3.

This project demonstrates how Python and boto3 can be used to automate AWS infrastructure monitoring in a DevOps environment.

---

# ✨ Features

### EC2 Inventory

* Retrieve EC2 instance details
* Instance Name
* Instance ID
* Instance State
* Instance Type
* Public IP
* Private IP
* Availability Zone
* Launch Time

### CloudWatch Monitoring

* CPU Utilization
* Network In
* Network Out
* Disk Read Bytes
* Disk Write Bytes
* Status Checks

### EBS Monitoring

* Volume ID
* Volume Size
* Volume Type
* Encryption Status
* Volume State

### Health Monitoring

* Healthy
* Warning
* Critical

### Report Generation

* CSV Report
* Excel Report
* JSON Report

### Amazon S3 Integration

* Automatically uploads generated reports to an S3 bucket

### Infrastructure Summary

* Total Instances
* Running Instances
* Stopped Instances

### Logging

* Application logging
* Error handling
* AWS API exception handling

---

# 🏗️ Project Architecture

```
Python
   │
   ▼
boto3
   │
   ▼
AWS APIs
   │
   ├── EC2
   ├── CloudWatch
   ├── EBS
   └── S3
   │
   ▼
Infrastructure Analysis
   │
   ▼
Reports
(CSV | Excel | JSON)
   │
   ▼
Upload to Amazon S3
```

---

# 📂 Project Structure

```
aws-infrastructure-health-monitor/

│
├── config/
│   └── config.py
│
├── logs/
│   └── app.log
│
├── modules/
│   ├── cloudwatch_metrics.py
│   ├── ec2_inventory.py
│   ├── ebs_details.py
│   ├── health_checker.py
│   ├── logger.py
│   ├── report_generator.py
│   └── s3_upload.py
│
├── reports/
│   ├── infrastructure_report.csv
│   ├── infrastructure_report.xlsx
│   └── infrastructure_report.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

* Python 3
* boto3
* pandas
* openpyxl

---

# ☁️ AWS Services Used

* Amazon EC2
* Amazon CloudWatch
* Amazon EBS
* Amazon S3
* IAM

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/aws-infrastructure-health-monitor.git
```

Go to the project directory

```bash
cd aws-infrastructure-health-monitor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

# ⚙️ Configuration

Update `config/config.py`

```python
AWS_REGION = "eu-north-1"

S3_BUCKET = "your-s3-bucket-name"
```

---

# 🔐 IAM Permissions Required

The EC2 instance or IAM user should have permissions for:

* ec2:DescribeInstances
* ec2:DescribeVolumes
* cloudwatch:GetMetricStatistics
* s3:PutObject

For testing, you can use:

* AmazonEC2ReadOnlyAccess
* CloudWatchReadOnlyAccess
* AmazonS3FullAccess

For production, use a custom IAM policy with least privilege.

---

# 📊 Sample Console Output

```
============================================================
AWS Infrastructure Health Monitor
============================================================

Name               : Jenkins
State              : running

CPU Utilization    : 12.4 %

Network In         : 542300 Bytes
Network Out        : 421000 Bytes

Disk Read Bytes    : 21000 Bytes
Disk Write Bytes   : 15000 Bytes

Health Status      : Healthy

Attached Volumes

Volume ID          : vol-0123456789
Volume Size        : 20 GB
Volume Type        : gp3

============================================================
Infrastructure Summary
============================================================

Total Instances    : 2
Running Instances  : 2
Stopped Instances  : 0

============================================================
```

---

# 📄 Generated Reports

The application automatically generates:

```
reports/

infrastructure_report.csv

infrastructure_report.xlsx

infrastructure_report.json
```

These reports are also uploaded to the configured Amazon S3 bucket.

---

# 🎯 Learning Outcomes

This project demonstrates:

* Python Programming
* AWS Automation
* boto3 SDK
* EC2 Inventory Management
* CloudWatch Monitoring
* EBS Management
* Amazon S3 Integration
* Report Generation
* Logging
* Exception Handling
* IAM Roles
* Infrastructure Monitoring

---

# 🚀 Future Enhancements

* Amazon SNS Email Notifications
* CloudWatch Alarms
* HTML Dashboard
* Scheduled Execution with EventBridge
* Docker Containerization
* CI/CD using Jenkins or GitHub Actions

---

# 👨‍💻 Author

**Suraj Singh R**

If you found this project helpful, consider giving it a ⭐ on GitHub.
