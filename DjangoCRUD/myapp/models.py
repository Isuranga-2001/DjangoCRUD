from django.db import models


# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=20, primary_key=True)
    uname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = "User"
