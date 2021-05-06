from django.contrib.auth import admin
from django.db import models


class Image(models.Model):
    PRIVACY = (('Public', 'Public'), ('Private', 'Private'))

    file_name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='uploads/')
    privacy = models.CharField(max_length=200, choices=PRIVACY, default='Private')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(admin.User, null=True, on_delete=models.SET_NULL, related_name="image")

    def __str__(self):
        return self.file_name
