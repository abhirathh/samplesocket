from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('placeOrder', views.placeOrder, name = 'placeOrder'),
    path('chatLogsJson', views.chatLogsJson, name = 'chatLogsJson'),
    path('userchats', views.userChatLogsJson, name = 'userChatLogsJson'),
    path('systemchats', views.systemChatLogsJson, name = 'systemChatLogsJson'),
    path('chatApp', views.chatApp, name = 'chatApp'),
    path('realTime', views.realTime, name = 'realTime'),
    path('dataBackup', views.dataBackup, name = 'dataBackup'),
    path('userData', views.userData, name = 'userData'),
]
