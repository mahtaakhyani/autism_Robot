# Generated by Django 3.0 on 2022-02-13 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HooshangCommands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.CharField(blank=True, default='normal', max_length=25)),
                ('dir', models.IntegerField(default=0)),
                ('pos_up', models.IntegerField(blank=True, default=530)),
                ('pos_right', models.IntegerField(blank=True, default=500)),
                ('right_hand', models.IntegerField(blank=True, default=200)),
                ('left_hand', models.IntegerField(blank=True, default=874)),
                ('speed', models.IntegerField(blank=True, default=250)),
                ('theta', models.IntegerField(blank=True, default=0)),
                ('yaw', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]