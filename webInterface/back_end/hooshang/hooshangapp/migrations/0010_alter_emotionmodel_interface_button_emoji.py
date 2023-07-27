# Generated by Django 3.2.12 on 2022-08-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hooshangapp', '0009_alter_emotionmodel_interface_button_emoji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotionmodel',
            name='interface_button_emoji',
            field=models.CharField(choices=[('bi-emoji-laugh', '😂'), ('bi-emoji-neutral', '🙄'), ('bi-emoji-laughing', '😄'), ('bi-emoji-frown', '🙁'), ('bi-emoji-surprised', '😳'), ('bi-emoji-sunglasses', '😎'), ('bi-emoji-angry', '😡'), ('bi-emoji-smile', '😊')], max_length=25),
        ),
    ]
