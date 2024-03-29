# Generated by Django 3.2.12 on 2022-08-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundsapp', '0002_alter_song_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.TextField(default='Unknown'),
        ),
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.CharField(default='Unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(default='No Image', upload_to=''),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.TextField(default='Unknown'),
        ),
    ]
