import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField

# Choices for gender
gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

# Create your models here.


class Customer(models.Model):
    '''
    Basic Details of Customer so that a Customer object can be created
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=gender)
    address = models.TextField()
    phone = PhoneNumberField(null=False, unique=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    '''
    Basic Details of Products so that a Product object can be created
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    price = MoneyField(max_digits=8, decimal_places=2, default_currency='INR')
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class Cart(models.Model):
    '''
    Basic Details of cart so that a cart object can be created
    and customer and products are linked as Foriegn key. 
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ForeignKey(
        Products, on_delete=models.CASCADE)
    order_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
