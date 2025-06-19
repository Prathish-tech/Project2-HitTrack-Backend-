from django.db import models
from django.contrib.auth.models import User

class Shot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Practice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shot = models.ForeignKey(Shot, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.user.username} - {self.shot.name}"

