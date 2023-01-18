from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path("secretadmin/", admin.site.urls),
    # User management
    path("accounts/", include("django.contrib.auth.urls")),
    # Local apps
    path("", include("pages.urls")),
    path("accounts/", include("accounts.urls")),
    path("desserts/", include("desserts.urls")),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
