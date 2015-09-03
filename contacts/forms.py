from django import forms
from contacts import models


class ContactForm(forms.ModelForm):
	class Meta:
		model = models.Contact
		exclude = ['user']
	# def save(self, usuario=None):
	# 	self.instance.user = usuario
	# 	super(ContactForm, self).save()
