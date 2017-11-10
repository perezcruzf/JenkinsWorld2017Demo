#!/usr/bin/python


# import boto3
import os
import json

#queue_url = "https://sqs.eu-west-2.amazonaws.com/860708036433/JenkinsWorldDemo" 

access_key = os.environ['AWS_ACCESS_KEY_ID']
secret_key = os.environ['AWS_SECRET_ACCESS_KEY']

# sqs_client = boto3.client('sqs', region_name='eu-west-2')

sqs_message = "{\n The Access Key ID is: " + access_key + ",\n   The Secret Access Key is: " + secret_key + "\n}"
print sqs_message
# sqs_client.send_message(QueueUrl=queue_url, MessageBody=sqs_message, MessageGroupId="1", MessageDeduplicationId="2")
