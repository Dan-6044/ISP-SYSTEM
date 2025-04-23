from django.db import models
from django.utils import timezone

class MikroTik(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ip_address = models.GenericIPAddressField()
    provisioned = models.BooleanField(default=False)
    provision_start_time = models.DateTimeField(null=True, blank=True)  # New field
