"""address_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from contacts.views import list_contacts, add_contact, login_user, edit_contact, log_out, delete_contact
from contacts import urls as contacts_urls
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', list_contacts, name='list_contacts'),
    url(r'^login_user/$', login_user, name='login_user'),
    url(r'^log_out/$', log_out, name='log_out'),
    url(r'^contact/', include(contacts_urls)),

]
