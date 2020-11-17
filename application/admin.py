from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import *


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (
                    'is_student',
                )
            },

        )
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Student)