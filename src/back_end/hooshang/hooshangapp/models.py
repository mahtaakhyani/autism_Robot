from django.db import models
from django.contrib.auth.models import User
from soundsapp.models import Song

# Create your models here.
class EmotionModel(models.Model):
    face = models.CharField(max_length= 25, blank=True, default= "normal", null=False, unique=True) #Types : normal , laugh, upset, surprise, shy
    face_video_url = models.CharField(max_length=200, blank=True, default="http://172.18.133.241:3000/mahta.mp4", null=False)
    sound = models.ForeignKey(Song, on_delete=models.CASCADE, blank=True, null=True)
    choices_tuple = (
        ('😂','😂'), ('🙄','🙄'), ('😄','😄'),
        ('🙁','🙁'), ('😱','😱'), ('😎','😎'),
        ('😡','😡'), ('😅','😅'),('😐','😐'),
        ('🤩','🤩'), ('😊','😊'), ('🤭','🤭'),
        ('😧','😧'), ('😳','😳'),  ('😌','😌'),
    )

    interface_button_emoji = models.CharField(max_length=25,choices=choices_tuple)

    def __str__(self):
        return self.face

    # dynatype = models.ForeignKey(HooshangCommandsDyna, on_delete=models.CASCADE)
    # movement = models.BooleanField(blank=False , null=False, default= False)
    
    # dir = models.IntegerField(blank=False, null=False, default=0) # 0 or 1 as: (up - right) or (down - left) --> For both Head & Hands commands

    # pos_up = models.IntegerField(blank=True, null=False, default=530) # Neck pitch turn
    # pos_right = models.IntegerField(blank=True, null=False, default=500) # Neck yaw turn   !!Head doesn't have any roll movement!!
    # # --> Neck pos values: default value for each (+/-) 5,445,600 for pitch & yaw spin)

    # right_hand = models.IntegerField(blank=True, null=False, default=200) # Right hand movement positioning (200 for no movement at all / 200 (+/-) 2,10,1020 for up & down movement)
    # left_hand = models.IntegerField(blank=True, null=False, default=874) # Right hand movement positioning (874 for no movement at all / 874 (+/-) 2,10,1020 for up & down movement)

    # # Defining vars plus their default values to be serialized as needed (--> serializers.py)
    # speed = models.IntegerField(blank=True, null=False, default=250)
    # theta = models.IntegerField(blank=True, null=False, default=0)
    # yaw = models.IntegerField(blank=True, null=False, default=0)
    