from django.db import models


class Order(models.Model):
    number = models.PositiveIntegerField(verbose_name='№', primary_key=True, blank=True)
    order_number = models.PositiveIntegerField(verbose_name='заказ №', blank=True)
    price_usd = models.DecimalField(verbose_name='стоимость,$', blank=True, max_digits=7, decimal_places=2)
    date = models.DateField(verbose_name='срок поставки', blank=True)
    price_rub = models.DecimalField(verbose_name='стоимость в руб.', blank=True, max_digits=9, decimal_places=2)
    date_is_expired = models.BooleanField(default=False)

class ExchangeRate(models.Model):
    rate = models.DecimalField(verbose_name='курс в руб.', blank=True, max_digits=7, decimal_places=4)
    update_at = models.DateTimeField(verbose_name='дата/время обновления', auto_now=True, blank=True)
