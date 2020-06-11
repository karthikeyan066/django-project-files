from django.contrib import admin
from .models import Register_form, breakfast_option, lunch_option, dinner_option

# Register your models here.
admin.site.register(Register_form),
admin.site.register(breakfast_option),
admin.site.register(lunch_option),
admin.site.register(dinner_option)