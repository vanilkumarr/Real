from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','id','email','subject','phone']
    list_display_links=['name','id']
    search_fields=["name",'email',"subject"]
    list_per_page=25
admin.site.register(Contact,ContactAdmin)