from django.db import models
from django.core.files.storage import Storage

# Create your models here.
class Song(models.Model):
    title= models.CharField(max_length=20,default='Unknown')
    description = models.TextField(max_length=50, blank=True, null=True)
    audio_file = models.FileField(upload_to='sounds/', blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20,default='Unknown')
    
    # def path(self):
    #     return self.audio_file

    def url(self):
        return str(self.audio_link)

    def __str__(self):
        return self.title


