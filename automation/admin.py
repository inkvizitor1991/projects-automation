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
        'email',
        'discord_username',
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


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    fields = ['id', 'name', 'start_date', 'end_date']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Command, CommandAdmin)
admin.site.register(Category)
admin.site.register(ProjectManager)
admin.site.register(ParticipantProject)
