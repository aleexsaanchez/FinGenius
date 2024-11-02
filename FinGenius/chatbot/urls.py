from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatview, name='chat'),
    path('feedback/', views.feedbackview, name='feedback'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]