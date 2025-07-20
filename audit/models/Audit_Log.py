from django.db import models
from accounts.models import UserModel

class AuditLog(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    action = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=20)
    details = models.CharField(max_length=20)