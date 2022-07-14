import boto3
import uuid

from django.conf  import settings

class S3Client:
    def __init__(self, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id     = AWS_ACCESS_KEY_ID,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        )

    def upload(self, file):
        url = 'img'+'/'+uuid.uuid4().hex
        
        self.s3_client.upload_fileobj(
            file, 
            "wegodang", 
            url, 
            ExtraArgs={
                "ContentType": file.content_type
            }
        )
        return url

class FileUploader:
    def __init__(self, client):
        self.client = client
    
    def upload(self, file):
        return self.client.upload(file)

s3_client        = S3Client(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)

s3_file_uploader = FileUploader(s3_client)