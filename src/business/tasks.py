from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *
# from django.contrib import messages
from async_messages import message_user
from authtools.admin import User
from django.contrib.messages import constants


@shared_task
def task_api_update_products(userid):
    try:
        user = User.objects.get(pk=userid)
        pfCatalogProduct.api_pull()
        message_user(
            user, 'Success! Product Catalog has been updated.', constants.SUCCESS)
    except Exception as e:
        message_user(user, 'API call failed. {}'.format(e), constants.ERROR)
