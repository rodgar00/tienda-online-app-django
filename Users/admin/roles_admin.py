from django.contrib import admin
from Users.models import Role

@admin.register(Role) #--> lo mismo que usando admin.site.register()
class RolesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    list_filter = ("is_active",)

    fieldsets = (
        ("Información del rol", {
            "fields": ("name", "slug", "is_active"),
        }),
    )