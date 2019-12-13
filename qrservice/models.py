from django.db import models
import uuid
from .choices import STATUSES
from .managers import QRcodeManager

class QRCode(models.Model):
    image = models.ImageField(upload_to='')
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    zone = models.ForeignKey('QRZone', on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField()


class QRZone(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField()




class Feedback(models.Model):
    qr_id = None
    text = models.CharField(max_length=512)
    name = models.CharField(max_length=128, blank=True)
    contact = models.CharField(max_length=48, blank=True)
    status = models.IntegerField(choices=STATUSES, default=1)
    objects = models.Manager()
    active_objects = QRcodeManager()




# class QRcode(models.Model):
#     unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     zone = models.ForeignKey('QRzone', on_delete=models.CASCADE)
# # Create your models here.
