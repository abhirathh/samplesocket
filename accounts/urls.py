from django.urls import path
from accounts import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('profile', views.profile, name='profile'),
    # path('register-2', views.register2, name='register2'),
    # path('gettoken', CustomAuthToken.as_view()),
]
