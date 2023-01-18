from django.urls import path
from .views import ItemListView
from .views import ItemDetailView

urlpatterns = [
  path('', ItemListView.as_view()),
  path('<int:pk>/', ItemDetailView.as_view())
]