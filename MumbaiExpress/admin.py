from django.contrib import admin
from .models import SignupModel,LoginModel,ContactusModel,OrderModel,OrdertableModel,Ordersqr

# Register your models here.


admin.site.register(SignupModel)
admin.site.register(LoginModel)
admin.site.register(ContactusModel)
admin.site.register(OrderModel)
admin.site.register(OrdertableModel)
admin.site.register(Ordersqr)