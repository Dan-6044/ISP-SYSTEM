# models.py
from django.db import models

class MikroTik(models.Model):
    name = models.CharField(max_length=255)
    provisioning_command = models.TextField(blank=True, null=True)
    provisioning_status = models.CharField(max_length=50, default='Pending')  # Can be 'Pending', 'Provisioning', 'Successful'
    is_ppoe = models.BooleanField(default=False)  # True for PPPoE, False for Hotspot

    def __str__(self):
        return self.name
