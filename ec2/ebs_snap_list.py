# List EBS snapshots older than 30 days
import datetime
import sys
import boto3
ec2 = boto3.client('ec2')
snapshots = ec2.describe_snapshots(OwnerIds=['self'], MaxResults=30)
if len (snapshots['Snapshots']) == 0:
    print ("No EBS snapshots were found")
retention_in_days = 30
def age(create_date):
    create_date_obj = create_date.replace(tzinfo=None)
    date_diff = datetime.datetime.now() - create_date_obj
    return date_diff.days

def snapshot_list():
    count = 0
    for snapshot in snapshots['Snapshots']:
        create_date = snapshot['StartTime']
        snapshot_id = snapshot['SnapshotId']
        snapshot_age = age(create_date)
        if snapshot_age < retention_in_days:
            count = count + 1
            print ("Snapshot Id: {} is {} days old".format(snapshot_id, snapshot_age))     
    if count == 0:
        print ("No snapshots were found older than {} days".format(retention_in_days))
snapshot_list()