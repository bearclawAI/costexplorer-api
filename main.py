import boto3

client = boto3.client('ce')

response = client.get_cost_and_usage_with_resources()
    
