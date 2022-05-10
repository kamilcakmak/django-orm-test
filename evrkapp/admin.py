from django.contrib import admin
admin.autodiscover()
admin.site.enable_nav_sidebar = False
admin.site.site_header = "EVREKA"
# Register your models here.
from .models import *

admin.site.register(Vehicle)

class NavigationrecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'datetime', 'latitude', 'longitude')
admin.site.register(Navigationrecord, NavigationrecordAdmin)

class BinAdmin(admin.ModelAdmin):
    exclude = ('id',)
admin.site.register(Bin, BinAdmin)

class OperationAdmin(admin.ModelAdmin):
    list_display = ('bin', 'last_collection', 'collection_frequency')

admin.site.register(Operation1, OperationAdmin)
admin.site.register(Operation2, OperationAdmin)