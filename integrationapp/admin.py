from django.contrib import admin

from .models import Trello
from .models import Discord


admin.site.register(Trello)
admin.site.register(Discord)
