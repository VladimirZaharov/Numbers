import datetime

import xml.etree.ElementTree as ET
from time import sleep

import requests
from django.core.management import BaseCommand

import orders
from orders.models import ExchangeRate


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            exchange_rate = self.get_exchange_rate()
            try:
                db_rate = ExchangeRate.objects.latest('update_at')
                if exchange_rate == float(db_rate.rate):
                    db_rate.update_at = datetime.datetime.now()
                    db_rate.save()
                else:
                    db_rate = ExchangeRate.objects.create(rate=exchange_rate)
                    db_rate.save()
            except ExchangeRate.DoesNotExist:
                db_rate = ExchangeRate.objects.create(rate=exchange_rate)
                db_rate.save()

            sleep(3600)

    def get_exchange_rate(self):
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        today = datetime.datetime.today()
        ago = datetime.timedelta(days=4)
        period = today - ago
        today.strftime("%m/%d/%Y")
        req = requests.get(f'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={period.strftime("%d/%m/%Y")}&'
                           f'date_req2={today.strftime("%d/%m/%Y")}&VAL_NM_RQ=R01235', headers=headers)
        exchange_rate = float(tuple(tuple(ET.fromstring(req.content))[-1])[-1].text.replace(',', '.'))
        return exchange_rate