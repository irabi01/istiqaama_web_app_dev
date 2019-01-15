from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import MemberInfo, Dependant_info

# Register your models here.
@admin.register(MemberInfo)
class ViewAdmin(ImportExportModelAdmin):
    pass
@admin.register(Dependant_info)
class ViewAdmin(ImportExportModelAdmin):
    pass
