from django.db import models
from django.contrib.auth.models import User
from . import choices

class Contact(models.Model):
    name = models.CharField('Nombre', max_length=255)
    last_name = models.CharField('Apellidos', max_length=255, blank=True, null=True)
    address = models.CharField('Direccion', max_length=255, blank=True, null=True)
    email = models.EmailField('Correo', blank=True, null=True)
    type_number = models.IntegerField('Tipo', choices=choices.TYPE_NUMBER_CHOICES)
    number = models.IntegerField('Numero')
    user = models.ForeignKey(User)

    def __unicode__(self): #__str__ python 3
        return "{0} {1}".format(self.name, self.last_name)
