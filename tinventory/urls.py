from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
                  path("", include("ui.urls")),

                  path('admin/', admin.site.urls),
                  path('api-auth/', include('rest_framework.urls')),
                  path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
