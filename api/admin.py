from django.contrib import admin
from.models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display=('pid',)


admin.site.register(Package,PackageAdmin)