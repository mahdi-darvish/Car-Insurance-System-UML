from django.core.mail import send_mail
from main.models import Notification_table, Policy_table

class Notification:
    def __init__(self):
        self.title = 'insurance'
        self.policies = []
        

    def check(self):
        list_policy =  Policy_table.objects.all()
        for item in list_policy:
            left = (item.end_date - item.start_date).days
            if left < 6:
                self.policies.append(item)
        
        self.check()

 
    def send(self):
        receivers = []
        for item in self.policies:
            receivers.append(item.email)
        send_mail(
        self.title,
        'Your Insurance is about to expire, Please recharge it a soon as possible.',
        'ganj.ashkan@gmail.com',
        ['AshkanGanj@gmail.com'],
        fail_silently=False)
        print('sent')

