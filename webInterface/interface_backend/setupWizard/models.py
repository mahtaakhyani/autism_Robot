from django.db import models

# Create your models here.
class MotorConfig(models.Model):
    choices_tuple = (('Type','Servo'),('Type','DC'), ('Type','Stepper'))
    type = models.CharField(max_length=25,choices=choices_tuple)

class JointConfig(models.Model):
    dofs = models.ManyToManyField(MotorConfig)

class ExpressiveFeatures(models.Model):
    emofacial = models.BooleanField(default=False)
    
class TalkingFeatures(models.Model):
    nlp = models.BooleanField(default=False)
    tts = models.BooleanField(default=False)
    emospeech = models.BooleanField(default=False)

class ListeningFeatures(models.Model):
    streaminput = models.BooleanField(default=False)
    saveinput = models.BooleanField(default=False)
    voicefeatureextraction = models.BooleanField(default=False)

class MovingFeatures(models.Model):
    pass

class FeaturesConfig(models.Model):
    hear = models.ForeignKey(ListeningFeatures, on_delete=models.CASCADE)
    talk = models.ForeignKey(TalkingFeatures, on_delete=models.CASCADE)
    express = models.ForeignKey(ExpressiveFeatures, on_delete=models.CASCADE)
    move = models.ForeignKey(MovingFeatures, on_delete=models.CASCADE)


class RobotConfig(models.Model):
    name = models.CharField(max_length=255, default="My_Robot" )
    features = models.ManyToManyField(FeaturesConfig, default=[])
    joints = models.ManyToManyField(JointConfig)

