from django.contrib import admin
from setupWizard import models as mdls
# Register your models here.

admin.site.register(mdls.ExpressiveFeatures)
admin.site.register(mdls.TalkingFeatures)
admin.site.register(mdls.ListeningFeatures)
admin.site.register(mdls.MovingFeatures)
admin.site.register(mdls.JointConfig)
admin.site.register(mdls.FeaturesConfig)
admin.site.register(mdls.MotorConfig)
admin.site.register(mdls.RobotConfig)