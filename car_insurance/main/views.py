from django.shortcuts import render
from django.http import HttpResponse

# Customer


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

# Car


def addCar(request):
    return render(request, 'Car/create.html', {})


def editCar(request):
    return render(request, 'Car/edit.html', {})


def getCar(request):
    return render(request, 'Car/get.html', {})


def listCars(request):
    return render(request, 'Car/list.html', {})


def deleteCar(request):
    return render(request, 'Car/delete.html', {})
# ---------------------------

# policy


def addPolicy(request):
    return render(request, 'insurance/create.html', {})


def editPolicy(request):
    return render(request, 'insurance/edit.html', {})


def getPolicy(request):
    return render(request, 'insurance/get.html', {})


def listPolicies(request):
    return render(request, 'insurance/list.html', {})


def deletePolicy(request):
    return render(request, 'insurance/delete.html', {})
# ---------------------------
