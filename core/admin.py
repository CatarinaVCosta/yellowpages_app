from django.contrib import admin
from .models import Company

# Register your models here.


# class CompanyAdmin(admin.ModelAdmin):
#     fields = ['name', 'phone', 'address', 'postal_code', 'district', 'url', 'photo', 'description', 'category']
#     list_display = ['name', 'phone', 'address', 'district', 'category']
#     search_fields = ['category', 'district']


admin.site.register(Company)
