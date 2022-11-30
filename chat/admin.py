from django.contrib import admin
from .models import chatLogs, userChatLogs, systemChatLogs

admin.site.register(chatLogs)
admin.site.register(userChatLogs)
admin.site.register(systemChatLogs)
