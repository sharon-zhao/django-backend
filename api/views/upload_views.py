from django.shortcuts import render
from django.views.generic import FormView

from .forms import S3DirectUploadForm
import uuid
import boto3

S3_BASE_URL='https://s3-us-east-1.amazonaws.com'
BUCKET='django-sharon'

class MyView(FormView):
    template_name = 'form.html'
    form_class = S3DirectUploadForm
