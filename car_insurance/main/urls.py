from django.urls import path
from . import views


urlpatterns = [
    path('', views.listCustomers, name='index'),
    path('customer/add', views.addCustomer, name='addCustomer'),
    path('customer/edit', views.editCustomer, name='editCustomer'),
    path('customer/editProfile', views.editCustomerProfile, name='editCustomerProfile'),
    path('customer/get', views.getCustomer, name='getCustomer'),
    path('customer/list', views.listCustomers, name='listCustomers'),
]