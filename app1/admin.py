from django.contrib import admin
from .models import Content,Contact
# Register your models here.
# admin.site.register(Content)
# admin.site.register(Contact)

class contentadmin(admin.ModelAdmin):
    list_display=['name','phone','address','city','state','pincode']
admin.site.register(Content,contentadmin)




class contactadmin(admin.ModelAdmin):
    list_display=['fname','lname','email','msg']
admin.site.register(Contact,contactadmin)