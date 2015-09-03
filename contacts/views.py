from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import pprint
from . import forms
from . import models

# def list_contacts(request):
#     if request.user.is_authenticated():
#         list_contacts = get_list_or_404(models.Contact, user=request.user)
#         return render(request, 'contacts/list_contacts.html', {'list_contacts' : list_contacts})
#     else:
#         return redirect(reverse('login_user'))

class ListContacts(ListView):
    template_name = 'contacts/list_contacts.html'
    context_object_name  = 'list_contacts'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = models.Contact.objects.filter(user=request.user)
        return super(ListContacts, self).dispatch(request, *args, **kwargs)

def login_user(request):
    template_response = 'contacts/login.html'
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('list_contacts'))
        else:
            messages.error(request, u'Usuario/Password incorrecto')
            return render(request, template_response, {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, template_response, {'form': form})
def log_out(request):
    logout(request)
    return redirect(reverse('login_user'))

def singup(request):
    template_response = 'contacts/singup.html'
    if request.method=='POST':
        print "dddddd"
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login_user'))
        else:
            return render(request, template_response, {'form': form})
    else:
        form = UserCreationForm()
        return render(request, template_response, {'form': form})


# def add_contact(request):
#     if request.method == 'POST':
#         contact_form = forms.ContactForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save(usuario=request.user)
#             return HttpResponse('guardado')
#         else:
#             return render(request, 'contacts/add_contact.html', {'contact_form' : contact_form})
#
#     contact_form = forms.ContactForm()
#     return render(request, 'contacts/add_contact.html', {'contact_form' : contact_form})


# def edit_contact(request, id_contact):
#     contact_instance = get_object_or_404(models.Contact, id=id_contact)
#
#     if request.method == 'POST':
#         contact_form = forms.ContactForm(request.POST, instance=contact_instance)
#
#         if contact_form.is_valid():
#             contact_form.save(usuario=request.user)
#             return HttpResponse('actualizado')
#         else:
#             return render(request, 'contacts/add_contact.html', {'contact_form' : contact_form})
#
#     contact_form = forms.ContactForm(instance=contact_instance)
#     return render(request, 'contacts/add_contact.html', {'contact_form' : contact_form})

# def delete_contact(request, id_contact):
#     contact = get_object_or_404(models.Contact, id=id_contact)
#     contact.delete()
#     return redirect(reverse('list_contacts'))


# class EditContact(View):
#     def post(self, request, id_contact):
#         contact_instance = get_object_or_404(models.Contact, id=id_contact)
#         contact_form = forms.ContactForm(request.POST, instance=contact_instance)
#
#         if contact_form.is_valid():
#             contact_form.save(usuario=request.user)
#             return HttpResponse('actualizado')
#         else:
#             return render(request, 'contacts/add_contact.html', {'contact_form' : contact_form})
#
#     def get(self, request, id_contact):
#         contact_instance = get_object_or_404(models.Contact, id=id_contact)
#         contact_form = forms.ContactForm(instance=contact_instance)
#         return render(request, 'contacts/add_contact.html', {'contact_form' : contact_form})

class AddContact(CreateView):
    template_name = 'contacts/add_contact.html'
    model = models.Contact
    form_class = forms.ContactForm
    success_url = reverse_lazy('list_contacts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddContact, self).form_valid(form)


class EditContact(UpdateView):
    template_name = 'contacts/add_contact.html'
    form_class = forms.ContactForm
    success_url = reverse_lazy('list_contacts')
    slug_field = 'id'
    slug_url_kwarg = 'id_contact'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = models.Contact.objects.filter(id=self.kwargs['id_contact'])
        return super(EditContact, self).dispatch(request, *args, **kwargs)

class DeleteContact(DeleteView):
    model = models.Contact
    success_url = reverse_lazy('list_contacts')
    form_class = forms.ContactForm
    slug_field = 'id'
    slug_url_kwarg = 'id_contact'
    template_name_suffix = ''

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = models.Contact.objects.filter(id=self.kwargs['id_contact'])
        request.method = 'POST'
        return super(DeleteContact, self).dispatch(request, *args, **kwargs)
