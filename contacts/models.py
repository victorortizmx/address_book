from django.db import models
from . import choices

class Contact(models.Model):
  name         =  models.CharField(max_length=50)
  last_name    =  models.CharField(max_length=100, null=True, blank=True)
  email        =  models.EmailField(max_length=100)
  phone_number =  models.CharField(max_length=20)
  type_number  =  models.PositiveIntegerField(choices=choices.TYPE_NUMBER_CHOICES)
  address      =  models.CharField(max_length=255)
  person       =  models.ForeignKey('Person', null=True)
  groups       =  models.ManyToManyField('groups.Group')

  def __unicode__(self):
    return self.name

class Person(models.Model):
  name = models.CharField(max_length=50)

  def __unicode__(self):
    return self.name
