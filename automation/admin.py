from django.contrib import admin
from .models import (
     Category,
    Student, ProjectManager,
    Command, ParticipantProject
)





class ParticipantProjectInline(admin.TabularInline):
    model = ParticipantProject
    extra = 0


class CommandAdmin(admin.ModelAdmin):

    inlines = [
        ParticipantProjectInline
    ]

admin.site.register(Command, CommandAdmin)
admin.site.register(Category)
admin.site.register(Student)
admin.site.register(ProjectManager)
admin.site.register(ParticipantProject)
