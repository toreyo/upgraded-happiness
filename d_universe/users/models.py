from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #can also add bio's, locations, and all kinds of other stuff to this field

    def __str__(self):
        return f'{self.user.username} Profile'


# Create your models here.
