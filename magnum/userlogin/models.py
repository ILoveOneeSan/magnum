from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('User ID', max_length=120)
    password = models.CharField('User Pass', max_length=120)

    def _str_(self):
        return self.name
        return self.password
