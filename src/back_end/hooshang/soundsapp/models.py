from django.db import models

# Create your models here.
class Song(models.Model):
    title= models.TextField(default='Unknown')
    artist= models.TextField(default='Unknown')
    image= models.ImageField(default='No Image')
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20,default='Unknown')
    paginate_by = 2

    def __str__(self):
        return self.title


