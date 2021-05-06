from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>', views.post_detail, name='post_detail'),
    path('search', views.search, name='search'),
    path('delete/', views.delete, name='delete'),
    path('<int:id>/delete/', views.confirm_delete, name='confirm_delete'),
]
