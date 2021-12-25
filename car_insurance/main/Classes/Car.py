from main import models
from main.models import Car_table, Customer_table


class Car:
    def __init__(self, engineNum, model, yearOfManufacture):
        self.engineNum = engineNum
        self.model = model
        self.yearOfManufacture = yearOfManufacture

    def add(self, customer_id):
        flag = False
        items = Car_table.objects.values_list('engine_number')
        for item in items:
            if int(item[0]) == int(self.engineNum):
                flag = True
                return flag
        cust = Customer_table.objects.get(customer_id=customer_id)
        Car_table.objects.create(customer_id=cust, engine_number=self.engineNum, model=self.model, manufacture_year=self.yearOfManufacture)
        return flag

    @staticmethod
    def get(engine_number):
        cust = Car_table.objects.filter(engine_number=engine_number)
        return cust

    def edit(self, engineNum):
        car = Car_table.objects.filter(engine_number=engineNum).update(model = self.model, manufacture_year=self.yearOfManufacture)
        return car
    
    @staticmethod
    def delete(engineNum):
        flag = True
        items = Car_table.objects.values_list('engine_number')
        for item in items:
            if int(item[0]) == int(engineNum):
                flag = False
                car = Car_table.objects.get(engine_number=engineNum)
                car.delete()
                return flag
        return flag
        # policy should deleted too
        

    @staticmethod
    def list():
        return Car_table.objects.all()