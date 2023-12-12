Working and implementation of Infrastructure as a service.

pip install boto3
import boto3
from botocore.exceptions import NoCredentialsError

def create_ec2_instance():
    # Specify your AWS credentials and region
    aws_access_key = 'YOUR_ACCESS_KEY'
    aws_secret_key = 'YOUR_SECRET_KEY'
    aws_region = 'YOUR_REGION'

    # Specify the AMI (Amazon Machine Image) ID for the desired operating system
    ami_id = 'ami-xxxxxxxxxxxxxxxxx'  # Replace with a valid AMI ID

    # Specify the instance type (e.g., t2.micro for a free tier eligible instance)
    instance_type = 't2.micro'

    # Specify the key pair name (you should have the private key for this key pair)
    key_pair_name = 'your-key-pair'

    # Create an EC2 client
    ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

    try:
        # Launch EC2 instance
        response = ec2.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1,
            KeyName=key_pair_name
        )

        # Print the instance ID
        instance_id = response['Instances'][0]['InstanceId']
        print(f'EC2 instance launched. Instance ID: {instance_id}')

    except NoCredentialsError:
        print('Credentials not available')

if _name_ == '_main_':
    create_ec2_instance()