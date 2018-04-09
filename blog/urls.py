from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('category/<int:pk>/', views.PostsByCategoryView.as_view(), name='category'),   
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),   
    path('', views.IndexView.as_view(), name='list'),
]
