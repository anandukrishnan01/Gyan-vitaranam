from django.contrib import admin
from .models import Marklist,Student_Details,ImageConverter
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.admin import ImportExportMixin
# Register your models here.

admin.site.register(ImageConverter)

admin.site.register(Student_Details)

class Studentdata(resources.ModelResource):

    class Meta:
        model = Student_Details

    def __init__(self, form_fields=None):
        super().__init__()
        self.form_fields = form_fields

    def get_export_fields(self):
        return [self.fields[f] for f in self.form_fields]


@admin.register(Marklist)
class collegeadmin(ImportExportModelAdmin):
    pass

# class BookAdmin(ImportExportMixin, admin.ModelAdmin):
#     list_display = ('Student_name', 'Department', 'Roll_no')
#     # list_filter = ['categories', 'author']
#     resource_class = Studentdata

#     def get_export_resource_kwargs(self, request, *args, **kwargs):
#         formats = self.get_export_formats()
#         form = collegeadmin(formats, request.POST or None)
#         # get list of fields from form (hard-coded to 'author' for example purposes)
#         form_fields = ("Student_name",)
#         return {"form_fields": form_fields}