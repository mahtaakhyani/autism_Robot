from django.db.models import fields
from rest_framework import serializers
from hooshangapp import models


# Hooshang dynamixels-grouped movement(Head - hands - transition) serilizing
# class HooshangDynaSerializerHead(serializers.ModelSerializer):

#     class Meta:
#         model = models.EmotionModel
#         fields = ('id','pos_up','pos_right')

# class HooshangDynaSerializerHands(serializers.ModelSerializer):

#     class Meta:
#         model = models.EmotionModel
#         fields = ('id','right_hand','left_hand')

# class HooshangDynaSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.EmotionModel
#         fields = ('id','speed','theta','yaw')

class EmotionModelSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = models.EmotionModel
        fields = ("id","face","sound","file_url") #('id','face','sound')	
    
    def get_file_url(self, document):
        request = self.context.get('request')
        file_url = document
        print(request.build_absolute_uri(file_url))
        return request.build_absolute_uri(file_url)
