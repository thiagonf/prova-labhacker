from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from authentication.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('auth/', include('authentication.urls')),
    path('', include('dashboard.urls')),
]
