from django.urls import path
from .views import RedPacketListView, RedPacketDetailView

urlpatterns = [
  path('', RedPacketListView.as_view()),
  path('<int:pk>/', RedPacketDetailView.as_view())
]