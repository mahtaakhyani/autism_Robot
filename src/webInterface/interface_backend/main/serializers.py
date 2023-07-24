from django.db.models import fields
from rest_framework import serializers
from main import models


# interface_backend dynamixels-grouped movement(Head - hands - transition) serilizing
# class interface_backendDynaSerializerHead(serializers.ModelSerializer):

#     class Meta:
#         model = models.EmotionModel
#         fields = ('id','pos_up','pos_right')

# class interface_backendDynaSerializerHands(serializers.ModelSerializer):

#     class Meta:
#         model = models.EmotionModel
#         fields = ('id','right_hand','left_hand')

# class interface_backendDynaSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.EmotionModel
#         fields = ('id','speed','theta','yaw')

class EmotionModelSerializer(serializers.ModelSerializer):
    # file_url = serializers.SerializerMethodField()

    class Meta:
        model = models.EmotionModel
        fields = ("id","face","sound",) #("file_url",'id','face','sound')	
    
    # def get_fiS