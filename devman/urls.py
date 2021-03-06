from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from automation.views import page_no_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('automation.urls')),
    path('integrations/', include('integrationapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_no_found
