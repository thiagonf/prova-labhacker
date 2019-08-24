from django.urls import path, include
from authentication.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', include('social_django.urls', namespace='social')),
]
