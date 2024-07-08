from django.db import models

# Create your models here.



# python manage.py makemigrations
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title