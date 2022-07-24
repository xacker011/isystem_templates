from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=150)
    month = models.IntegerField(default=3)
    day = models.IntegerField()
    price = models.IntegerField(default=0)
    desc = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
