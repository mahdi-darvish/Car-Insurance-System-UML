from django.contrib import admin

from .models import Car, Insurance_Agent, Policy, Customer, Notification

admin.site.register(Car)
admin.site.register(Insurance_Agent)
admin.site.register(Policy)
admin.site.register(Customer)
admin.site.register(Notification)
