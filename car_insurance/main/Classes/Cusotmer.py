from django.db.models.expressions import F
from main.models import Customer_table

class Customer:
    def __init__(self, address, name, email, phone):
        self.address = address
        self.name = name
        self.email = email
        self.phone = phone

    def create(self):
        flag = False
        emails = Customer_table.objects.values_list('email')
        for email in emails:
             if email[0] == self.email:
                flag = True
                return flag
        cust = Customer_table.objects.create(customer_name=self.name, address=self.address, email=self.email, phone=self.phone)
        return flag

    def get(self, customerID):
        pass

    def update(self, customerID):
        pass

    def updateProfile(self):
        pass

    def list(self):
        pass