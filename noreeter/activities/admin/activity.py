from django.contrib import admin

from activities.models import Activity


@admin.register(Activity)
class ActivityModelAdmin(admin.ModelAdmin):
    pass
