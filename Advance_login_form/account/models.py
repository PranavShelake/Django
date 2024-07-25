from django.db import models
from django.contrib.auth.models import User

class account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    security_key = models.CharField(max_length=10)

    def __str__(self):
        return self.user.email
