from django.contrib import admin
from .models import Tienda,Zona, UserProfile


# Add in this class to customized the Admin Interface
class ZonaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

admin.site.register(Tienda)
admin.site.register(Zona,ZonaAdmin)
admin.site.register(UserProfile)