from django.shortcuts import render
from django.http import HttpResponse

def addCustomer(request):
    return render(request, 'Customer/create.html', {})


def editCustomer(request):
    return render(request, 'Customer/edit.html', {})


def editCustomerProfile(request):
    return render(request, 'Customer/editProfile.html', {})


def getCustomer(request):
    return render(request, 'Customer/get.html', {})


def listCustomers(request):
    return render(request, 'Customer/list.html', {})



def deleteCare(request):
    return render(request, 'Car/delete.html', {})
