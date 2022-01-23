from django.contrib import admin

from .models import Trello
from .models import TrelloBoard
from .models import Discord


@admin.register(Trello)
class TrelloAdmin(admin.ModelAdmin):
    pass


@admin.register(TrelloBoard)
class TrelloAdmin(admin.ModelAdmin):
    pass


@admin.register(Discord)
class DiscordAdmin(admin.ModelAdmin):
    pass
