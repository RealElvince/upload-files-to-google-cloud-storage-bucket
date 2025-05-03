from create_bucket import keyfile_path,storage_client, BUCKET_NAME

upload_file_path = keyfile_path

upload_client = storage_client

# function to upload a file to the bucket
def upload_file_to_gcs(bucket_name, source_file_name, destination_blob_name):
      # reference bucket
    bucket=storage_client.bucket(bucket_name)
    # create a blob object from the file path
    blob = bucket.blob(destination_blob_name)
     # Check if the file already exists
    if blob.exists():
        print(f" File already exists in GCS: gs://{bucket_name}/{destination_blob_name}. Skipping upload.")
        return
    # upload files
    try:
      blob.upload_from_filename(source_file_name)

      print(f"File {source_file_name} uploaded to the gs://{bucket_name}/{destination_blob_name}")
    except Exception as e:
      print(f"Error in uploading file {e}")

# set local files and their destination paths in the bucket
files_to_upload={
      'health_data/patients.csv':'prod/health_data/patients.csv',
      'health_data/doctors.csv':'prod/health_data/doctors.csv',
      'health_data/appointments.csv':'prod/health_data/appointments.csv',
      'health_data/medical_records.csv':'prod/health_data/medical_records.csv',
      'health_data/invoices.csv':'prod/health_data/invoices.csv'
  }

# call upload_file_to_gcs function
for local_file,destination_blob in files_to_upload.items():
    upload_file_to_gcs(BUCKET_NAME,local_file,destination_blob)

print('All files uploaded successfully!')
    