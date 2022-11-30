from django.db import models

class chatLogs(models.Model):
    username = models.CharField(max_length = 255, default = 0)
    user_chat = models.CharField(max_length = 255, default = 0)
    system_chat = models.CharField(max_length = 255, default = 0)
    symbol = models.CharField(max_length = 255, default = 0)
    type = models.CharField(max_length = 255, default = 0)
    oms_order_id = models.CharField(max_length = 255, default = 0)
    price = models.CharField(max_length = 255, default = 0)
    product = models.CharField(max_length = 255, default = 0)
    quantity = models.CharField(max_length = 255, default = 0)
    filled_quantity = models.CharField(max_length = 255, default = 0)
    order_status = models.CharField(max_length = 255, default = 0)
    rejection_reason = models.CharField(max_length = 255, default = 0)

    def __str__(self):
        return self.username


class userChatLogs(models.Model):
    username = models.CharField(max_length = 255, default = 0)
    user_chat = models.CharField(max_length = 255, default = 0)
    symbol = models.CharField(max_length = 255, default = 0)
    type = models.CharField(max_length = 255, default = 0)
    oms_order_id = models.CharField(max_length = 255, default = 0)
    price = models.CharField(max_length = 255, default = 0)
    product = models.CharField(max_length = 255, default = 0)
    quantity = models.CharField(max_length = 255, default = 0)
    filled_quantity = models.CharField(max_length = 255, default = 0)
    order_status = models.CharField(max_length = 255, default = 0)
    rejection_reason = models.CharField(max_length = 255, default = 0)

    def __str__(self):
        return self.username

class systemChatLogs(models.Model):
    username = models.CharField(max_length = 255, default = 0)
    system_chat = models.CharField(max_length = 255, default = 0)
    symbol = models.CharField(max_length = 255, default = 0)
    type = models.CharField(max_length = 255, default = 0)
    oms_order_id = models.CharField(max_length = 255, default = 0)
    price = models.CharField(max_length = 255, default = 0)
    product = models.CharField(max_length = 255, default = 0)
    quantity = models.CharField(max_length = 255, default = 0)
    filled_quantity = models.CharField(max_length = 255, default = 0)
    order_status = models.CharField(max_length = 255, default = 0)
    rejection_reason = models.CharField(max_length = 255, default = 0)

    def __str__(self):
        return self.username
