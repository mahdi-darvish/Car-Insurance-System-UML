from django.shortcuts import render, redirect
from django.http import HttpResponse
from main import models
from main.Classes.Cusotmer import Customer
from main.Classes.Car import Car
from .models import Car_table



# Customer


def addCustomer(request):
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
    return render(request, 'Customer/edit.html', {'error':error, 'success':success, 'prompt': prompt})



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

    return render(request, 'Customer/get.html', {'error':error, 'success':success})


def listCustomers(request):
    results = Customer.list()
    return render(request, 'Customer/list.html', {'results': results})


# Car
def addCar(request):
    error = ''
    success = ''
    cust_list = Customer.list()
    if request.method=="POST":
        customer_id = request.POST.get('customerID')
        engine_number = request.POST.get('engine_number')
        model = request.POST.get('model')
        manufacture_year = request.POST.get('manufacture_year')
        car = Car(engine_number, model, manufacture_year)
        response = car.add(customer_id)
        if response:
            error = 'Car Engine already exist.'     
        else:
            success = 'Car, {}, successfully added.'.format(engine_number)

    return render(request, 'Car/create.html', {'error':error, 'success':success, 'cust_list': cust_list})


def editCar(request):
    error = ''
    success = ''
    prompt = ''
    engine_number = None
    if request.method=="GET":
        engine_number = request.GET.get('engine_number')
        car = Car.get(engine_number)
        if not car:
            error = 'Car Engine number not found.'
        else:
            success = car[0]

    if request.method=="POST":
        engine_number = request.POST.get('engineNum')
        model = request.POST.get('model')
        manufacture_year = request.POST.get('yearOfManufacture')

        car = Car(engine_number, model, manufacture_year)
        car.edit(engine_number)
        prompt = 'Car with Engine number {}, successfully updated.'.format(engine_number)
    print(success)
    print(error)
    print(prompt)
    return render(request, 'Car/edit.html', {'error':error, 'success':success, 'prompt': prompt})


def getCar(request):
    error = ''
    success = ''
    if request.method=="POST":
        engine_number = request.POST.get('engine_number')
        car = Car.get(engine_number)
        if not car:
            error = 'Engine Number not found'
        else:
            success = car
    print(error)
    print(success)
    return render(request, 'Car/get.html', {'error':error, 'success':success})


def listCars(request):
    results = Car.list()
    print(results)
    return render(request, 'Car/list.html', {'results': results})


def deleteCar(request):
    error = ''
    success = ''
    if request.method=="POST":
        engine_number = request.POST.get('engine_number')
        car = Car.delete(engine_number)
        if car:
            error = 'Engine Number not found'
        else:
            success = 'Car {} successfully deleted'.format(engine_number)
    print(error)
    print(success)
    return render(request, 'Car/delete.html', {})
# ---------------------------

# policy


def addPolicy_cust(request):
    error = ''
    success = ''
    if request.method=="POST":
        cust_id = request.POST.get('CustomerID')
        customer = Customer.get(cust_id)
        if not customer:
            error = 'Customer ID not founD.'
        else:
            return redirect('/insurance/add/{}'.format(cust_id))

    return render(request, 'insurance/create.html', {})

def addPolicy_car(request, customer_id):
    cars = Car_table.objects.filter(customer_id=customer_id)
    if request.method=="POST":
        customer_id = request.POST.get('customerID')
        engine_number = request.POST.get('cars')
        price = request.POST.get('price')
        status = True
        type = request.POST.get('cars')
        # car = Car(engine_number, model, manufacture_year)
        # response = car.add(customer_id)
        # if response:
        #     error = 'Car Engine already exist.'     
        # else:
        #     success = 'Car, {}, successfully added.'.format(engine_number)
    return render(request, 'insurance/create_2.html', {'customer_id': customer_id, 'cars': cars})


def editPolicy(request): 
    return render(request, 'insurance/edit.html', {})


def getPolicy(request):
    return render(request, 'insurance/get.html', {})


def listPolicies(request):
    return render(request, 'insurance/list.html', {})


def deletePolicy(request):
    return render(request, 'insurance/delete.html', {})
# ---------------------------
