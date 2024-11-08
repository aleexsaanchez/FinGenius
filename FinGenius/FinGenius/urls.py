from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path
from chatbot import views as chatbot_views

urlpatterns = [
    path('', chatbot_views.aboutview, name='home'),
    path('admin/', admin.site.urls),
    path('login/', chatbot_views.login_view, name='login'),
    path('chatbot/', chatbot_views.chatview, name='chatbot'),
    path('about/', chatbot_views.aboutview, name='about'),
    path('feedback/', chatbot_views.feedbackview, name='feedback'),
    path('register', chatbot_views.register_view, name='register'),
    path('profile/', chatbot_views.profile_view, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
