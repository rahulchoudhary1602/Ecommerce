from django.contrib import admin
from .models import Cart, cartitem
# Register your models here.
admin.site.register(Cart)

admin.site.register(cartitem)
