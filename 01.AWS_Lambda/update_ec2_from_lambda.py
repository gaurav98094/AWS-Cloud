import json
import boto3
from botocore.exceptions import WaiterError

def wait_until_instance_stopped(ec2_client,instance_id):
    waiter = ec2_client.get_waiter('instance_stopped')
    
    try:
        waiter.wait(InstanceIds=[instance_id])
    except WaiterError as e:
        print(f'Error : {e}')

def lambda_handler(event, context):
    # TODO implement
    instance_id = event['instanceId']
    
    ec2_client = boto3.client('ec2')
    
    try:
        ec2_client.stop_instances(InstanceIds=[instance_id])
        wait_until_instance_stopped(ec2_client,instance_id)
        # ec2_client.modify_instance_attribute(InstanceId = instance_id,InstanceType={'Value':'t2.medium'})
        # ec2_client.start_instances(InstanceIds=[instance_id])
    except Exception as e:
        print(e)