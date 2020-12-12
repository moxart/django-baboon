from django.urls import path

from . import views

app_name = 'contact'
urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
]
