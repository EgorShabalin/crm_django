from django.contrib import admin


from .models import *


admin.site.register(Student)
admin.site.register(Representative)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Subject)
# admin.site.register(Contractor)
admin.site.register(Contract)
admin.site.register(Payment)
admin.site.register(Document)
admin.site.register(Residence_permit)
admin.site.register(Order)
admin.site.register(Statement)
admin.site.register(Application)

"""
class PhotoAdmin(admin.TabularInline):
    model = Photo


class StudentAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]

    class Meta:
        model = Student
"""

admin.site.register(Photo)
