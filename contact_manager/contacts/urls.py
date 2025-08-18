from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/add/', views.add_contact, name='add_contact'),
    path('contacts/edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
]
