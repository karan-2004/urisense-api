from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='strips/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created_at'

class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='results')
    chemical = models.CharField(max_length=20)
    red = models.IntegerField()
    green = models.IntegerField()
    blue = models.IntegerField()
