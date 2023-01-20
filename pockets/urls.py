from django.urls import path
from .views import PocketListView, PocketDetailView

urlpatterns = [
  path('', PocketListView.as_view()),
  path('<int:pk>/', PocketDetailView.as_view())
]