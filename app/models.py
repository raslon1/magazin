from django.db import models
import uuid
from colorful.fields import RGBColorField
# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    guid = models.UUIDField(primary_key=True, unique = True, editable=False, default=uuid.uuid4)
    parent = models.ForeignKey('self', verbose_name='Родитель', blank = True, null = True, on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, unique=True)
    guid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    hexcode = RGBColorField()

    class Meta():
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
    
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    guid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    color = models.ForeignKey(Color, verbose_name = 'Цвет', on_delete = models.CASCADE)
    category = models.ForeignKey(Category, verbose_name = 'Категория', on_delete = models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Цена')
    class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self):
        return self.name