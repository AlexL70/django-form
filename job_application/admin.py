from django.contrib import admin
from .models import JobAppForm


class JobAppFormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email",
                    "start_date", "occupation")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("start_date", "occupation")
    ordering = ("last_name", "first_name")
    readonly_fields = ("first_name", "last_name", "email")


admin.site.register(JobAppForm, JobAppFormAdmin)
