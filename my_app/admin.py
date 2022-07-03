from django.contrib import admin
from . import models
# Register your models here.


# Registering Customer models to admin
admin.site.register(models.Customer)
# Registering Products models to admin
admin.site.register(models.Products)
# Registering Order models to admin
admin.site.register(models.Cart)

