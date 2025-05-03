from google.cloud import storage

keyfile_path ="/gcp/service_account.json"

storage_client = storage.Client.from_service_account_json(keyfile_path)

BUCKET_NAME = "healthcare-test-bucket"

# Create the bucket
def create_bucket(bucket_name):
    buckets = storage_client.list_buckets()
    for bucket in buckets:
        if bucket.name == bucket_name:
            print(f"Bucket {bucket_name} already exists")
            return
    
    try:
        bucket = storage_client.create_bucket(bucket_name, location="US")
        print(f"Bucket {bucket.name} created")
    except Exception as e:
        print(f"Failed to create bucket: {e}")

create_bucket(BUCKET_NAME)
