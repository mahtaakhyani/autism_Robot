# Generated by Django 3.2.12 on 2022-09-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hooshangapp', '0010_alter_emotionmodel_interface_button_emoji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotionmodel',
            name='face',
            field=models.CharField(blank=True, default='normal', max_length=25, unique=True),
        ),
    ]