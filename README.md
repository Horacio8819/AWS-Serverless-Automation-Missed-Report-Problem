# AWS Serverless Automation – Missed Report Problem

## Overview

This project solves a common data pipeline issue where analysts are not notified when new reports are uploaded.

Using AWS serverless services, the system automatically sends an email notification whenever a new file is uploaded to an S3 bucket.

Event-driven automation and alerting using AWS S3, Lambda, and SNS.

## Architecture

Client Upload → S3 Bucket → Lambda Function → SNS Topic → Email Notification

## AWS Services Used

* Amazon S3 – Storage for uploaded reports
* AWS Lambda – Automation logic
* Amazon SNS – Email notifications

## How It Works

1. A client uploads a report to the S3 bucket.
2. S3 triggers the Lambda function.
3. Lambda extracts the file name and bucket name.
4. Lambda sends a message to SNS.
5. SNS sends an email notification to subscribed analysts.

## Benefits

* Eliminates manual monitoring of report folders
* Ensures analysts receive data immediately
* Prevents delays in dashboard generation
* Uses cost-efficient serverless architecture

## Example Notification

Subject: New Report Uploaded

New file uploaded: s3://insightdata-reports-hg/sales_report.csv


Cloud Engineering Workshop – Serverless Automation Lab

# Challenges

- How does it scale if 1000 clients upload at once?
- Should we use Slack or EventBridge for faster response?
- How can I add monitoring, retries, or logging?

## Scenario:
The client’s analysts rely on these reports to generate dashboards by 9 AM.
Tomorrow, no one uploads anything to the bucket.
The analysts show up at 9 AM, nothing happens.
No error. No alert. Silence.

## 💭Think through:
- What AWS service could run once a day to check for missing files?
- How would it verify that no new data came in?
- What’s the business cost of silence?
