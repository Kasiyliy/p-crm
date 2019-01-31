from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Наименование')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Создан')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование товара')
    quantity = models.IntegerField(verbose_name='Количество')
    price = models.IntegerField(verbose_name='Цена')
    status = models.BooleanField(verbose_name='В наличии')
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Создан')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Client(models.Model):
    client_name = models.CharField(max_length=100, verbose_name='Имя')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Создан')

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Order(models.Model):
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Создан')
    status = models.BooleanField(default=False, verbose_name='Принят')
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Вендор')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def get_total_cost(self):
        orderProducts = OrderProduct.objects.filter(order=self).all()
        price = 0
        for item in orderProducts:
            price += item.get_cost()
        return price
    get_total_cost.short_description = 'Сумма'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, related_name='product_title', on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.product.price * self.quantity

