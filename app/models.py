from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=20)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=20)
    site = models.CharField(max_length=300)


class PhoneModel(models.Model):
    ANDROID = 'Android'
    IOS = 'iOS'
    MS_WINDOWS = 'MSWin'
    SYMBIAN = 'Symbian'
    OS_CHOICES = (
        (ANDROID, 'Android'),
        (MS_WINDOWS, 'MS Windows Phone'),
        (IOS, 'iOS'),
        (SYMBIAN, 'Symbian'),
    )
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer)
    OS = models.CharField(max_length=100, choices=OS_CHOICES)
    CPU = models.IntegerField()
    core_num = models.IntegerField()
    sim_card_num = models.IntegerField()
    megapixels_num = models.FloatField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    p_model = models.ForeignKey(PhoneModel)
    price = models.FloatField()
    in_stock = models.IntegerField()


class Order(models.Model):
    client_id = models.ForeignKey(Client)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='OrderItem')


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def _get_total(self):
        return self.product.price * self.quantity
    total_cost = property(_get_total)
