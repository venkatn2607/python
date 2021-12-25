# reboot EC2 Instance
#import Modules
import boto3
#Importing EC2 Methods
ec2 = boto3.client('ec2')
#variables
id1 = "i-051d92c38cb42f765"
id2 = "i-01fa4a45b76189c56"
#reboot Logic
#Functions
def reboot(id):
    response = ec2.reboot_instances(InstanceIds=[id,],DryRun=False)
    print ("Reboot response is: {}".format(response))
    print ("Instance ID: {} is rebooted".format(id))
reboot(id1)
reboot(id2)