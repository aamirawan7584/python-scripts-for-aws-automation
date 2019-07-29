"""
import boto3

ec2 = boto3.resource('ec2')
# create a EC2 instance
instances = ec2.create_instances(
     ImageId='ami-0f378490dca16e3f4', # this image id is taken manually from aws dashboard
     MinCount=1,                      # minimum number of ec2 instances
     MaxCount=2,                      # maximum number of ec2 instances
     InstanceType='t2.micro',         # instance type it could be t2.micro, t2.small, m5.large
     KeyName='ec2-keypair'            # previous script generated key pair will be used here
)

"""

import logging
import boto3
from botocore.exceptions import ClientError


def create_ec2_instance(image_id, instance_type, keypair_name):
    """Provision and launch an EC2 instance

    The method returns without waiting for the instance to reach
    a running state.

    :param image_id: ID of AMI to launch, such as 'ami-XXXX'
    :param instance_type: string, such as 't2.micro'
    :param keypair_name: string, name of the key pair
    :return Dictionary containing information about the instance. If error,
    returns None.
    """

    # Provision and launch the EC2 instance
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.run_instances(ImageId=image_id,
                                            InstanceType=instance_type,
                                            KeyName=keypair_name,
                                            MinCount=1,
                                            MaxCount=1)
    except ClientError as e:
        logging.error(e)
        return None
    return response['Instances'][0]


def main():
    """Exercise create_ec2_instance()"""

    # Assign these values before running the program
    image_id = 'ami-02f706d959cedf892'
    instance_type = 't2.micro'
    keypair_name = 'ecc'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Provision and launch the EC2 instance
    instance_info = create_ec2_instance(image_id, instance_type, keypair_name)
    if instance_info is not None:
        logging.info('Launched EC2 Instance {instance_info["InstanceId"]}')
        logging.info('    VPC ID: {instance_info["VpcId"]}')
        logging.info('    Private IP Address: {instance_info["PrivateIpAddress"]}')
        logging.info('    Current State: {instance_info["State"]["Name"]}')


if __name__ == '__main__':
    main()
