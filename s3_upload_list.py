#import boto2
import boto3
#Input 
file = "server.log"

#List
buckets= ["venkat-aws","venkat-aws-2"]
#create client for s3 service
s3 = boto3.resource('s3')
# Data Processing
s3.meta.client.upload_file(file, buckets[0], "log/server.log")
print("File : {} uploaded to Bucket: {}".format(file,buckets[0]))

s3.meta.client.upload_file(file, buckets[1], "log/server.log")
print("File : {} uploaded to Bucket: {}".format(file,buckets[1]))