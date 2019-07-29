"""
Amazon EC2 uses public–key cryptography to encrypt and decrypt login information.
Public–key cryptography uses a public key to encrypt a piece of data, and then the
recipient uses the private key to decrypt the data.
The public and private keys are known as a key pair.
Public-key cryptography enables you to securely access your instances using a private key instead of a password.
"""

#script for accessing key pair for new ec2 instance

import boto3
ec2 = boto3.resource('ec2')

# create a file to store the key locally
outfile = open('ec2-keypair.pem','w')

# call the boto ec2 function to create a key pair
key_pair = ec2.create_key_pair(KeyName='ec2-keypair')

# capture the key and store it in a file
KeyPairOut = str(key_pair.key_material)
print(KeyPairOut)
outfile.write(KeyPairOut)
