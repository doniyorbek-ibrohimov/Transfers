from django.contrib import admin
from .models import *

admin.site.register(Season)
admin.site.register(Country)
admin.site.register(Player)
admin.site.register(Club)
admin.site.register(Transfer)

#media_settings

from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)