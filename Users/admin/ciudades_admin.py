from django.contrib import admin
from Users.models import CiudadModel

class CiuadadesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", )
    ordering = ("-name", )
    readonly = ("slug", )

admin.site.register(CiudadModel, CiuadadesAdmin)