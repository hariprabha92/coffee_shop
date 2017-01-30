import os
import json
from django.conf import settings
from bill.models import Order_detail,Order
from django.core.management.base import BaseCommand
from django.core import serializers


class Command(BaseCommand):

    def handle(self, *args, **options):
        print ("Loading model")
        d=list(Order_detail.objects.select_related('Order.id').values())
        d1=list(Order.objects.select_related('Order_detail.bill_id_id').values())

        print(d)
        print(d1)
 #       data=serializers.serialize("json",Order.objects.select_related('id').values())
       # data1=serializers.serialize("json",Order_detail.objects.select_related().all())

        print("LOADS ORDER TABLE")
        rows = json.dumps(d)
      #  print(rows)
        print("LOADS ORDER DETAILS TABLE")
       # rows = json.dumps(data1)
       # print(rows)
