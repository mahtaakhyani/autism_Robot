# Generated by Django 3.2.12 on 2022-08-21 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hooshangapp', '0002_emotionmodel_face_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotionmodel',
            name='face',
            field=models.CharField(blank=True, default='normal', max_length=25, null=True),
        ),
    ]
