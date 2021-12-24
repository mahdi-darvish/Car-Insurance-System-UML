from main.models import Customer_table

class Customer:
    def __init__(self, address, name, customerID, email, phone):
        self.address = address
        self.name = name
        self.customerID = customerID
        self.email = email
        self.phone = phone

    def create(self):
        flag = False
        x = Customer_table.values_list('emails')
        print(x)
        cust = Customer_table.create(self.name, self.address, self.email, self.phone)
        return cust

    def get(self, customerID):
        pass

    def update(self, customerID):
        pass

    def updateProfile(self):
        pass

    def list(self):
        pass