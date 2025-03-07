from django.db import models

class WhatsAppGroup(models.Model):
    group_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class GroupMember(models.Model):
    group = models.ForeignKey(WhatsAppGroup, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
