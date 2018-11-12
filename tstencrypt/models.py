from django.db import models
from fernet_fields import EncryptedTextField


class MyEncrypt(models.Model):
    username = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    memo = models.CharField(max_length=200)
    seed = EncryptedTextField()
    pub_date = models.DateTimeField('date updated')

    def __str__(self):
        return self.username

    def show_seed(self):
        return self.seed


class MyDetail(models.Model):
    username = models.ForeignKey(MyEncrypt, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    counter = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date detailed')

    def __str__(self):
        return self.description

    def how_many(self):
        return self.counter


