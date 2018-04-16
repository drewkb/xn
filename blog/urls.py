from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('category/<int:pk>/', views.PostsByCategoryView.as_view(), name='category'),   
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('best/', views.BestView.as_view(), name='best'),   
    path('about/', views.PageView.as_view(slug='about'), name='about'),   
    path('advert/', views.PageView.as_view(slug='advert'), name='advert'),   
    path('', views.IndexView.as_view(), name='list'),
]
