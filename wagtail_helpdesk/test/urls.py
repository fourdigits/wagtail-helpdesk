from django.contrib import admin
from django.urls import include, path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from wagtail_helpdesk.users.urls import urlpatterns as users_urlpatterns

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("", include(wagtail_urls)),
    path("", include(users_urlpatterns)),
]
