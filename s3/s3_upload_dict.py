#import boto2
import boto3
#Input 
file = "server.log"

#Dictionaty
buckets= {"bucket1":"venkat-aws", "bucket2":"venkat-aws-2"}
#create client for s3 service
s3 = boto3.resource('s3')

# Data Processing
s3.meta.client.upload_file(file, buckets['bucket1'], "log/server.log")
print("File : {} uploaded to Bucket: {}".format(file,buckets['bucket1']))

s3.meta.client.upload_file(file, buckets['bucket2'], "log/server.log")
print("File : {} uploaded to Bucket: {}".format(file,buckets['bucket2']))