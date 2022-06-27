import datetime
from pprint import pprint
from time import sleep
import json
import requests
from django.core.management import BaseCommand

from numbers_project.settings import SPREAD_SHEET_ID, API_KEY
from orders.models import Order, ExchangeRate


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            sleep(10)
            my_sheet = requests.get(f'https://sheets.googleapis.com/v4/spreadsheets/{SPREAD_SHEET_ID}?key={API_KEY}')
            data = json.loads(my_sheet.content)
            data = data['sheets'][0]['properties']

            my_sheet = requests.get(f'https://sheets.googleapis.com/v4/spreadsheets/{SPREAD_SHEET_ID}'
                                    f'/values/{data["title"]}!A1:{(chr(int(data["gridProperties"]["columnCount"]) + 64))}'
                                    f'{data["gridProperties"]["rowCount"]}?key={API_KEY}')
            data = json.loads(my_sheet.content)
            orders = Order.objects.all()
            orders.delete()
            exchange_rate = ExchangeRate.objects.latest('update_at')

            Order.objects.bulk_create(
                [Order(
                    number=number,
                    order_number=order_num,
                    price_usd=price_usd,
                    date=datetime.date(
                        year=int(date.split('.')[2]),
                        month=int(date.split('.')[1]),
                        day=int(date.split('.')[0])
                    ),
                    price_rub=int(price_usd)*float(exchange_rate.rate)
                ) for number, order_num, price_usd, date in data['values'][1:]]
            )
