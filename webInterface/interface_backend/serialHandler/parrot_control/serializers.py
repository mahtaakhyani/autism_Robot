from rest_framework import serializers
from parrot_control import models


class CommandCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommandCategory
        fields = ('identifier', 'button_color', 'display_order')
        read_only_fields = ('identifier', 'button_color', 'display_order')


class ParrotCommandSerializer(serializers.ModelSerializer):
    category = CommandCategorySerializer(many=False, read_only=True)
    class Meta:
        model = models.ParrotCommand
        fields = ('id', 'name','interface_button_emoji', 'title', 'category', 'tag', 'perform_time', 'priority', 'parrot_0', 'parrot_1')
        read_only_fields = ('id', 'name','interface_button_emoji', 'title', 'category', 'tag', 'perform_time', 'priority', 'parrot_0', 'parrot_1')


