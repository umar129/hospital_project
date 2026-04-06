from django.contrib import admin
from .models import Patients


@admin.register(Patients)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email', 'mobile', 'doctor']
    search_fields = ['name', 'email', 'mobile']
    list_filter = ['age', 'doctor']
    ordering = ['-id']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'age', 'mobile', 'email')
        }),
        ('Address', {
            'fields': ('address',)
        }),
        ('Medical Assignment', {
            'fields': ('doctor',)
        }),
    )