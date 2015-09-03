from django.conf.urls import url
from contacts.views import EditContact, AddContact, DeleteContact

urlpatterns = [
    url(r'^edit_contact/(?P<id_contact>\d{1,})/$', EditContact.as_view(), name='edit_contact'),
    url(r'^add_contact/$', AddContact.as_view(), name="add_contact"),
    url(r'^delete_contact/(?P<id_contact>\d{1,})/$', DeleteContact.as_view(), name="delete_contact"),
]
