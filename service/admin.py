from django.contrib import admin
from service.models import Contact
from service.models import Department



class ContactAdmin(admin.ModelAdmin):
    list_display=("full_name","email_id","subject","mob_num","message")

class DepartmentAdmin(admin.ModelAdmin):
    list_display=("department_name",)




admin.site.register(Contact,ContactAdmin)      
admin.site.register(Department,DepartmentAdmin)   
# Register your models here.
