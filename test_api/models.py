from django.db import models
from django.urls import reverse
# Create your models here.

class Test_form(models.Model):

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)

    def get_absolute_url(self):
        return reverse('profile-detail',kwargs={'pk':self.pk})

    def __str__(self):
        return "{} - {}".format(self.first_name, self.email)
