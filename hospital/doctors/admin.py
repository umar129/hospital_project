from django.contrib import admin
from .models import Doctors, Departments


@admin.register(Departments)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'dep_name']
    search_fields = ['dep_name']
    ordering = ['dep_name']


@admin.register(Doctors)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department', 'joining_date', 'salary']
    search_fields = ['name']
    list_filter = ['department', 'joining_date']
    ordering = ['-joining_date']
    fieldsets = (
        ('Doctor Information', {
            'fields': ('name', 'department')
        }),
        ('Employment Details', {
            'fields': ('joining_date', 'salary')
        }),
    )
