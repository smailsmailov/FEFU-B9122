from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
