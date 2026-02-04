from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tariff, UserSubscription, CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('phone',)
    fieldsets = UserAdmin.fieldsets + (
        ('Номер', {'fields': ('phone',)}),
    )

admin.site.register(Tariff)
admin.site.register(UserSubscription)
admin.site.register(CustomUser, CustomUserAdmin)