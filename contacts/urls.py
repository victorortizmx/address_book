from django.conf.urls import url
from contacts.views import edit_contact, add_contact, delete_contact

urlpatterns = [
    url(r'^edit_contact/(?P<id_contact>\d{1,})/$', edit_contact, name='edit_contact'),
    url(r'^add_contact/$', add_contact, name="add_contact"),
    url(r'^delete_contact/(?P<id_contact>\d{1,})/$', delete_contact, name="delete_contact"),
]
