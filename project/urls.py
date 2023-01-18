from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items/', include('items.urls')),
    path('api/users/', include('jwt_auth.urls')),
    path('api/comments/', include('comments.urls'))
]
