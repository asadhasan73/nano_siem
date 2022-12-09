from django.db import models

from .service import Service


class ServiceLog(models.Model):
    timestamp = models.DateTimeField(db_index=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, db_index=True)
    requested_service = models.TextField()
    ip = models.GenericIPAddressField()
    longitude = models.FloatField(null=True, db_index=True)
    latitude = models.FloatField(null=True, db_index=True)
    autonomous_system_organization = models.TextField(null=True)
    country_name = models.TextField(null=True)
    city_name = models.TextField(null=True)
    user = models.TextField()
    event = models.TextField()
    message = models.TextField()
    http_status = models.PositiveIntegerField(null=True)
    user_agent = models.TextField()
    request_method = models.CharField(max_length=10)
    content_size = models.PositiveBigIntegerField(null=True)
    is_tor = models.BooleanField(db_index=True)
    ids_score = models.PositiveIntegerField(default=0, db_index=True)
