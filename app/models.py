from django.db import models
from django.core.urlresolvers import reverse


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=20)
    site = models.CharField(max_length=300)

    def __str__(self):
        return '{}'.format(self.name)


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

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'pk': self.pk})

    def __str__(self):
        return '{}, OS: {}, Sim cards: {}'.format(self.name, self.OS, self.sim_card_num)


class Product(models.Model):
    name = models.CharField(max_length=200)
    p_model = models.ForeignKey(PhoneModel, verbose_name="Model info")
    price = models.FloatField()
    in_stock = models.IntegerField()

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'pk': self.pk})

    def __str__(self):
        return '{}'.format(self.name)


class Order(models.Model):
    client_id = models.ForeignKey(Client)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='OrderItem')

    def __str__(self):
        return '{} {} : {}'.format(self.client_id.name, self.client_id.surname, self.products)


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def _get_total(self):
        return self.product.price * self.quantity
    total_cost = property(_get_total)

    def __str__(self):
        return 'Order #{}, product: {} quantity: {}'.format(self.order.id, self.product.name, self.quantity)

