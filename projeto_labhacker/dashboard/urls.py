from django.urls import path
from dashboard.views import DashboardView, EditTagView

urlpatterns = [
    path(
        'dashboard/',
        DashboardView.as_view(),
        name='dashboard'),
    path(
        'tags/<str:name_repository>/',
        EditTagView.as_view(),
        name='edit_tag'),
]
