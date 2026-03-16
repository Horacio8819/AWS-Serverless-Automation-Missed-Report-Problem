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



# Automation Steps

Automatically notify analysts whenever a new sales report is uploaded.

Instead of manually checking folders, the system will automatically send an email.

## Architecture:

                                                   Sales Report Upload
                                                            │
                                                            ▼
                                                    Amazon S3 Bucket
                                                            │
                                                            ▼
                                                    S3 Event Trigger
                                                            │
                                                            ▼
                                                    AWS Lambda Function
                                                            │
                                                            ▼
                                                    Amazon SNS Topic
                                                            │
                                                            ▼
                                                    Email Notification

**Step 1: Create the Notification Channel (SNS)**
- In the AWS console, search for *SNS (Simple Notification Service)*.
- Click Topics → Create topic.
- Type: Standard
- Name: report-upload-alerts
- Click Create topic

Now let’s add an email address that will receive alerts:
- Click Create subscription
- Protocol: Email
- Endpoint: your email address
- Click Create subscription
- Check your inbox and Confirm subscription.

**Step 2: Create the Storage (S3)**
- Search for S3 in the AWS console → Create bucket
- Name: insightdata-reports-<your-initials>
- Region: pick one close to you.
- Leave everything else as default → Create bucket

Step 3: Create the Automation Function (Lambda)
- Search for Lambda → Create function
- Author from scratch
- Function name: new-report-notifier
- Runtime: Python 3.14
- Permissions: Choose "Create default role" ==> “Create new role with basic Lambda permissions”
- Click Create function

**When the function loads: Scroll to Code source → click the file name → paste the lambda_function.py**
**Deploy**

**Step 4: Give Lambda Access to SNS**
- Scroll down → Configuration → Permissions
- Click the Role name → it opens IAM.
- Click Add permissions → Attach policies.
- Search for and add:
**AmazonSNSFullAccess**
**AWSLambdaBasicExecutionRole**

Step 5: Add the SNS Topic to Lambda
- Go to your SNS topic page 
- Copy the Topic ARN (the long string starting with arn:aws:sns:)
- Go back to Lambda → Configuration → Environment variables
- Add:
      Key: TOPIC_ARN
      Value: (paste your topic ARN)

**Step 6: Connect the Trigger (S3 → Lambda)**
- In Lambda → Add trigger
- Source: S3
- Bucket: insightdata-reports-<your-initials>
- Event type: “All object create events.”

**Step 7: Test the Workflow**
- Go to S3 → your bucket → Upload file.


