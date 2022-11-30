from django.db import models

class userRegistration(models.Model):
    fname = models.CharField(max_length = 255, default = 0)
    lname = models.CharField(max_length = 255, default = 0)
    username = models.CharField(max_length = 255, default = 0)
    email = models.CharField(max_length = 255, default = 0)
    password = models.CharField(max_length = 255, default = 0)
    brokerUserId = models.CharField(max_length = 255, default = 0)
    brokerPwd = models.CharField(max_length = 255, default = 0)
    brokerSecretKey = models.CharField(max_length = 255, default = 0)
    brokerAppId = models.CharField(max_length = 255, default = 0)
    brokerTwoFA = models.CharField(max_length = 255, default = 0)

    def __str__(self):
        return self.username
