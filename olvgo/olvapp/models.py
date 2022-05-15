from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

# Create your models here.


class Customer(models.Model):



    order_id = models.TextField(max_length=20,unique=True)
    full_name = models.TextField(max_length=50)
    company = models.TextField(max_length=60,blank=True)
    email = models.EmailField(max_length=40)
    phone_number = models.TextField(max_length=17)
    note = models.TextField(max_length=256,blank=True)


    def __str__(self):
        return self.order_id
