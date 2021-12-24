from django.contrib import admin

from .models import Car_table, Car_table, Insurance_Agent_table, Policy_table, Customer_table, Notification_table

admin.site.register(Car_table)
admin.site.register(Insurance_Agent_table)
admin.site.register(Policy_table)
admin.site.register(Customer_table)
admin.site.register(Notification_table)
