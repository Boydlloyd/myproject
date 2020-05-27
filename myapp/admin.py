from django.contrib import admin
from .models import Computer,Operating_system
from .forms import ComputerForm
# Register your models here.


class ComputerAdmin(admin.ModelAdmin):
    list_display=['computer_name','IP_address','MAC_address','users_name','purchase_date','timestamp']
    form=ComputerForm
    list_filter=['computer_name','IP_address']
    search_fields = ['computer_name', 'IP_address','users_name']


admin.site.register(Computer,ComputerAdmin)
admin.site.register(Operating_system)