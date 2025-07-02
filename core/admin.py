from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Designer, BuyerRequest

@admin.register(Designer)
class DesignerAdmin(UserAdmin):
    model = Designer
    list_display = (
        'email',
        'first_name',
        'last_name',
        'business_name',
        'location',
        'specialty',
        'is_staff',
        'is_superuser'
    )
    list_filter = ('is_staff', 'is_superuser', 'specialty', 'location')
    search_fields = ('email', 'first_name', 'last_name', 'business_name')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'business_name', 'location', 'specialty')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'business_name',
                'location',
                'specialty',
                'password1',
                'password2',
                'is_staff',
                'is_superuser',
                'is_active',
                'groups',
                'user_permissions',
            ),
        }),
    )

    ordering = ('email',)

@admin.register(BuyerRequest)
class BuyerRequestAdmin(admin.ModelAdmin):
    list_display = ('phone', 'location', 'category', 'timestamp')
    search_fields = ('phone', 'location', 'category')
    list_filter = ('category', 'location')
