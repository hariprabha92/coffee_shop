import os
import json
from django.conf import settings
from bill.models import Order_detail,Order
from django.core.management.base import BaseCommand
from django.core import serializers


class Command(BaseCommand):

    def handle(self, *args, **options):
        print ("Loading model")
        data=serializers.serialize("json",Order.objects.all())
        data1=serializers.serialize("json",Order_detail.objects.all())

        print("LOADS ORDER TABLE")
        rows = json.dumps(data)
        print(rows)
        print("LOADS ORDER DETAILS TABLE")
        rows = json.dumps(data1)
        print(rows)
