from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    description = models.TextField()
    photo = models.ImageField(upload_to='media')
    address = models.ForeignKey('Address', on_delete=models.PROTECT, null=True)

class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=128)
    house_num = models.IntegerField()
    flat_num = models.IntegerField(null=True, blank=True)

class PhoneNumber(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=128)
    person = models.ForeignKey('Person', on_delete=models.PROTECT)

class Mail(models.Model):
    email = models.EmailField()
    type = models.CharField(max_length=128)
    person = models.ForeignKey('Person', on_delete=models.PROTECT)

class Group(models.Model):
    name = models.CharField(max_length=64)
    person = models.ManyToManyField(Person)
