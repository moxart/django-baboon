from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),

    path('post/<slug:slug>', views.PostSingleView.as_view(), name='post-single'),

    path('post/category/<slug:slug>/', views.PostCategoryView.as_view(), name='post-category'),
]
