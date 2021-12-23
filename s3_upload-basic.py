#import boto2
import boto3
#Input 
file = "server.log"
bucket1 = "venkat-aws"
bucket2 = "venkat-aws-2"
#create client for s3 service
s3 = boto3.resource('s3')
# Data Processing
s3.meta.client.upload_file(file, bucket1, "log/server.log")
## server.log uploaded to bucket
print("File : {} uploaded to Bucket: {}".format(file,bucket1))
s3.meta.client.upload_file(file, bucket2, "log/server.log")
print("File : {} uploaded to Bucket: {}".format(file,bucket2))