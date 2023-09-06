from django.db import models
from django.contrib.auth.models import User

class NewUserDetail(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=[('M','Male'),
    ('F','Female')])
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.user.username

   




