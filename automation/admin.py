from django.contrib import admin
from .models import (
    Project,
    Category,
    Student, ProjectManager,
    Command, ParticipantProject
)





@admin.register(Student)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'category',
        'far_east',
    ]
    list_filter = [
        'category',
        'far_east'
    ]




class ParticipantProjectInline(admin.TabularInline):
    model = ParticipantProject
    extra = 0


class CommandAdmin(admin.ModelAdmin):
    inlines = [
        ParticipantProjectInline
    ]



admin.site.register(Project)
admin.site.register(Command, CommandAdmin)
admin.site.register(Category)
admin.site.register(ProjectManager)
admin.site.register(ParticipantProject)
