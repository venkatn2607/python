# Input data type
import boto3

id1 = "i-051d92c38cb42f765"
id2 = "i-01fa4a45b76189c56"
status = 200
ec2 = boto3.client('ec2')

#Restart ec2
responce1 = ec2.reboot_instances(InstanceIds=[id1], DryRun=False)
if responce1['ResponseMetadata']['HTTPStatusCode'] == status:
    print ("instacne : {} is rebooted successfully".format(id1))
else:
    print ("instacne : {} Reboot is  fail".format(id1))

responce2 = ec2.reboot_instances(InstanceIds=[id2], DryRun=False)
print(type(responce2))