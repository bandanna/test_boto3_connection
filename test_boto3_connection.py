import boto3

# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

if(response['Buckets'] is not None and len(response['Buckets'])>0):
    print("\n===== Congrats, your connection is set! ======\n")