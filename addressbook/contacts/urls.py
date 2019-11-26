# from django.conf.urls import include, url

# from . import views

# urlpatterns = [
#     url(r'^$', views.index, name="index")
# ]

from django.conf.urls import url

from contacts.views import ContactsListView, ContactsDetailView, ContactsCreateView, ContactsDeleteView

urlpatterns = [
    url(r'^$', ContactsListView.as_view(template_name="home.html")),
    url(r'^contacts/(?P<pk>[0-9]+)/$', ContactsDetailView.as_view(template_name="contact_details.html")),
    url(r'^contacts/new', ContactsCreateView.as_view(template_name="new_contact.html")),
    url(r'^contacts/(?P<pk>[0-9]+)/delete/$', ContactsDeleteView.as_view(template_name="delete_contact.html")),
]