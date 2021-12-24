from django.db import models


class Customer_table(models.Model):

    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    address = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()


class Car_table(models.Model):

    customer_id = models.ForeignKey(Customer_table, on_delete=models.CASCADE)
    engine_number = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=50)
    manufacture_year = models.DateField()


class Insurance_Agent_table(models.Model):

    customer_id = models.ForeignKey(Customer_table, on_delete=models.CASCADE)
    agent_id = models.AutoField(primary_key=True)


class Policy_table(models.Model):

    customer_id = models.ForeignKey(Customer_table, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(Insurance_Agent_table, on_delete=models.CASCADE)
    engine_number = models.ForeignKey(Car_table, on_delete=models.CASCADE)
    policy_id = models.AutoField(primary_key=True)
    price = models.FloatField()
    status = models.BooleanField(default=True)
    type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()


class Notification_table(models.Model):

    policy_id = models.ForeignKey(Customer_table, on_delete=models.CASCADE, primary_key=True)
    date = models.DateTimeField(null=True)