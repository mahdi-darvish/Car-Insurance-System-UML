from django.shortcuts import render
from django.http import HttpResponse
from main.Classes.Cusotmer import Customer
from main.models import Customer_table



# Customer


def addCustomer(request):
    print(Customer_table.objects.first().customer_id)
    error = ''
    success = ''
    if request.method=="POST":
        email = request.POST.get('email')
        address = request.POST.get('address')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        cust = Customer(address, name, email, phone)
        response = cust.create()
        if response:
            error = 'Email already in use.'
        else:
            success = 'Customer, {}, successfully added.'.format(name)
    return render(request, 'Customer/create.html', {'error':error, 'success':success})


def editCustomer(request):
    error = ''
    success = ''
    prompt = ''
    cust_id = None
    if request.method=="GET":
        cust_id = request.GET.get('CustomerID')
        cust = Customer.get(cust_id)
        if not cust:
            error = 'Customer ID not found'
        else:
            success = cust[0]

    if request.method=="POST":
        cust_id = request.POST.get('CustomerID')
        email = request.POST.get('email')
        address = request.POST.get('address')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        print(cust_id)
        print(email)
        cust = Customer(address, name, email, phone)
        cust.update(cust_id)
        prompt = 'Customer number {}, successfully updated.'.format(cust_id)
        print(prompt)
    return render(request, 'Customer/edit.html', {'error':error, 'success':success, 'prompt': prompt})


def editCustomerProfile(request):
    return render(request, 'Customer/editProfile.html', {})


def getCustomer(request):
    error = ''
    success = ''
    if request.method=="POST":
        cust_id = request.POST.get('CustomerID')
        cust = Customer.get(cust_id)
        if not cust:
            error = 'Customer ID not found'
        else:
            success = cust
            print(success)

    return render(request, 'Customer/get.html', {'error':error, 'success':success})


def listCustomers(request):
    results = Customer.list()
    print(results)
    return render(request, 'Customer/list.html', {'results': results})

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
