# from django.shortcuts import render

# # Create your views here.

# def index(request):
#     return render(request, 'contacts/index.html')

from django.views.generic import ListView, DetailView, CreateView, DeleteView

from contacts.models import Contacts

class ContactsListView(ListView):
    model = Contacts
    template_name = 'home.html'

class ContactsDetailView(DetailView):
    model = Contacts
    template_name = 'contact_details.html'

class ContactsCreateView(CreateView):
    model = Contacts
    template_name = 'new_contact.html'
    fields = ['firstName', 'lastName', 'phoneNumber', 'email', 'streetAddress']

class ContactsDeleteView(DeleteView):
    model = Contacts
    template_name = 'delete_contact.html'
    
