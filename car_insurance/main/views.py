from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'Customer/index.html', {})


def addCustomer(request):
    return render(request, 'Customer/index.html', {})


def editCustomer(request):
    return render(request, 'Customer/index.html', {})


def editCustomerProfile(request):
    return render(request, 'Customer/index.html', {})


def deleteCustomer(request):
    return render(request, 'Customer/index.html', {})


def getCustomer(request):
    return render(request, 'Customer/index.html', {})


def listCustomers(request):
    return render(request, 'Customer/index.html', {})
