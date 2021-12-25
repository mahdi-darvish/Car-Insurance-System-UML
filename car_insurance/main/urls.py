from django.urls import path
from . import views


urlpatterns = [
    # customer
    path('', views.listCustomers, name='index'),
    path('customer/add', views.addCustomer, name='addCustomer'),
    path('customer/edit', views.editCustomer, name='editCustomer'),
    path('customer/get', views.getCustomer, name='getCustomer'),
    path('customer/list', views.listCustomers, name='listCustomers'),
    # car
    path('car', views.listCars, name='index'),
    path('car/add', views.addCar, name='addCar'),
    path('car/edit', views.editCar, name='editCar'),
    path('car/get', views.getCar, name='getCar'),
    path('car/list', views.listCars, name='listCars'),
    path('car/delete', views.deleteCar, name='deleteCar'),
    # Insurance
    path('insurance', views.listPolicies, name='index'),
    path('insurance/add', views.addPolicy_cust, name='addPolicy_cust'),
    path('insurance/add/<int:customer_id>', views.addPolicy_car, name='addPolicy_car'),
    path('insurance/edit', views.editPolicy, name='editPolicy'),
    path('insurance/delete', views.deletePolicy,
         name='deletePolicy'),
    path('insurance/get', views.getPolicy, name='getPolicy'),
    path('insurance/list', views.listPolicies, name='listPolicies'),
]
