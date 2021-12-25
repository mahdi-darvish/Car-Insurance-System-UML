from main.models import Policy_table, Customer_table, Car_table, Insurance_Agent_table

class Policy:
    def __init__(self, customerID, engineNumber, startDate, endDate, price, status, policyType):
        self.customerID = customerID
        self.engineNumber = engineNumber
        self.agentID = 1
        self.endDate = endDate
        self.startDate = startDate
        self.price = price
        self.status = status
        self.policyType = policyType

    def issuePolicy(self):
        flag = False
        engs = Policy_table.objects.values_list('engine_number')
        print(engs)
        for eng in engs:
             if int(eng[0]) == int(self.engineNumber):
                flag = True
                return flag
        customer = Customer_table.objects.get(customer_id=self.customerID)
        agent = Insurance_Agent_table.objects.get(agent_id=self.agentID)
        car = Car_table.objects.get(engine_number=self.engineNumber)
        cust = Policy_table.objects.create(customer_id=customer, agent_id=agent, engine_number=car, price=self.price, 
                                            status=self.status, type=self.policyType, start_date=self.startDate, end_date=self.endDate)
        return flag

    @staticmethod
    def get(policyID):
        policy = Policy_table.objects.filter(policy_id=policyID)
        return policy

    def edit(self, policyID):
        pass

    @staticmethod
    def delete(policyID):
        flag = True
        items = Policy_table.objects.values_list('policy_id')
        for item in items:
            if int(item[0]) == int(policyID):
                flag = False
                policy = Policy_table.objects.get(policy_id=policyID)
                policy.delete()
                return flag
        return flag

    @staticmethod
    def list():
        return Policy_table.objects.all()
