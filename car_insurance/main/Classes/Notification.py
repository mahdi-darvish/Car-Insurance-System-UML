from django.core.mail import send_mail
from main.models import Notification_table, Policy_table
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

class Notification:
    def __init__(self):
        self.title = 'insurance'
        
    def check(self):
        emails = []
        list_policy =  Policy_table.objects.all()
        now = datetime.now().date()

        for item in list_policy:
            left = (item.end_date - now).days
            if left < 6:
                emails.append(item.customer_id.email)
        return emails
    
    def send(self):
        receivers = self.check()
        subject = self.title
        sender = settings.EMAIL_HOST_USER
        message = 'your policy is about to end!'
        send_mail(subject, 
            message, sender, receivers)
        