from django.db import models


class Image(models.Model):
    file_name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='user_uploads')
    private = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.file_name
