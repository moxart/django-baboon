from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
]
