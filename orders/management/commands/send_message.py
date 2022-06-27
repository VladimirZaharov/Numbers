import datetime
from time import sleep

import telebot

from numbers_project.settings import TELEGRAM_TOKEN
from django.core.management import BaseCommand

from orders.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = telebot.TeleBot(TELEGRAM_TOKEN)

        @bot.message_handler(commands=['start'])
        def start_command(message):
            self.expired_orders = self.expired_orders()
            bot.send_message(
                message.chat.id,
                f'Здравствуйте, у вас {len(self.expired_orders)} просроченых заказов {self.unpack_orders()}'
            )
            while True:
                sleep(86400)
                bot.send_message(message.chat.id,
                f'На сегодня у вас {len(self.expired_orders)} просроченых заказов {self.unpack_orders()}')
        bot.polling(none_stop=True)

    def expired_orders(self):
        orders = Order.objects.filter(date__lt=datetime.datetime.now()).values('order_number')
        return orders

    def unpack_orders(self):
        if self.expired_orders:
            return ', '.join([str(order['order_number']) for order in self.expired_orders])
        else:
            return ''
