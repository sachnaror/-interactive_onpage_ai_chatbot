from django.db import models

class SubscriptionDocument(models.Model):
    user_name = models.CharField(max_length=50)
    offering_name = models.CharField(max_length=100)
    profile_name = models.CharField(max_length=50)
    document_name = models.CharField(max_length=150)
    status = models.CharField(max_length=30)
    executed_on = models.DateField(null=True, blank=True)
    download_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.offering_name} - {self.document_name}"
