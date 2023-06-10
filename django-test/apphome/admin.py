from django.contrib import admin
from .models import Customers
from .models import Restaurants
from .models import Inference

# Register your models here.
admin.site.register(Customers)
admin.site.register(Restaurants)
admin.site.register(Inference)
