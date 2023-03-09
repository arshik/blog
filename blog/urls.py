from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib import admin
from django.urls import path, include
from users import urls as users_urls
from posts import urls as posts_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/users/", include(users_urls)),
    path("api/posts/", include(posts_urls)),
]
