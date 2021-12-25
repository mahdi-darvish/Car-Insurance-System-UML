from django.core.mail import send_mail
from main.models import Notification_table

class Notification:
    def __init__(self, notif_id, title):
        self.notif_id = notif_id
        self.title = title

    def check():
        pass

    def send():
        send_mail(
        'Subject here',
        'Your Insurance is about to expire, Please recharge it a soon as possible.',
        'ganj.ashkan@gmail.com',
        ['to@example.com'],
        fail_silently=False,
)

