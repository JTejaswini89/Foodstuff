from django.db import models

class UserRegistrationModel(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    status = models.CharField(max_length=20, default='pending')  # optional field
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
