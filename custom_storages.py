'''Static file storage configuration'''
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage): #pylint: disable=W0223
    '''Static files location'''
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage): #pylint: disable=W0223
    '''Media files location'''
    location = settings.MEDIAFILES_LOCATION
