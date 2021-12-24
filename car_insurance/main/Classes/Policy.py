class Policy:
    def __init__(self, policyID, customerID, startDate, endDate, price, status, policyType):
        self.policyID = policyID
        self.customerID = customerID
        self.endDate = endDate
        self.startDate = startDate
        self.price = price
        self.status = status
        self.policyType = policyType

    def issuePolicy(self):
        pass

    def get(self, policyID):
        pass

    def edit(self, policyID):
        pass

    def delete(self, policyID):
        pass

    def list(self):
        pass
