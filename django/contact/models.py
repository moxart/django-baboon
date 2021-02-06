from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sended_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
