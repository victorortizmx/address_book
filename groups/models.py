from django.db import models
from django.contrib.auth.models import User
from contacts import models as contacts_models

class Group(models.Model):
    name = models.CharField('Nombre', max_length=255)
    description = models.CharField('Descripcion', max_length=255)
    user = models.ForeignKey(User)
    contact = models.ManyToManyField(contacts_models.Contact, verbose_name="Contactos")

    def __unicode__(self): #__str__ python 3
        return self.name
