from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicHandoutStorage(S3Boto3Storage):
    location = "media"
    default_acl = "public-read"
    file_overwrite = False
