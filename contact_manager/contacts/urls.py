from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/add/', views.add_contact, name='add_contact'),
    path('contacts/edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('contacts/delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
