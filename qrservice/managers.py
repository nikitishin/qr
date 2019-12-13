from .choices import STATUSES
from django.db import models


class QRcodeManager(models.Model):
    def get_qeryset(self):
        return seper(self, QRcodeManager).get_qeryset().filter(is_active=True)


