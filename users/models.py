from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Contact(models.Model):
    username= models.CharField(max_length=50)
    email_id=models.EmailField(max_length=100)
    Phone_no=models.IntegerField()
    Message=models.TextField()
    def __str__(self) -> str:
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile.pics')

    def _str_(self):
        return f'{self.user.username} Profile'      
        
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)    