# Generated by Django 2.2.3 on 2023-07-09 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpressiveFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emofacial', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FeaturesConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('express', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setupWizard.ExpressiveFeatures')),
            ],
        ),
        migrations.CreateModel(
            name='JointConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ListeningFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streaminput', models.BooleanField(default=False)),
                ('saveinput', models.BooleanField(default=False)),
                ('voicefeatureextraction', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MotorConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Type', 'Servo'), ('Type', 'DC'), ('Type', 'Stepper')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='MovingFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TalkingFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nlp', models.BooleanField(default=False)),
                ('tts', models.BooleanField(default=False)),
                ('emospeech', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RobotConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('features', models.ManyToManyField(to='setupWizard.FeaturesConfig')),
                ('joints', models.ManyToManyField(to='setupWizard.JointConfig')),
            ],
        ),
        migrations.AddField(
            model_name='jointconfig',
            name='dofs',
            field=models.ManyToManyField(to='setupWizard.MotorConfig'),
        ),
        migrations.AddField(
            model_name='featuresconfig',
            name='hear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setupWizard.ListeningFeatures'),
        ),
        migrations.AddField(
            model_name='featuresconfig',
            name='move',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setupWizard.MovingFeatures'),
        ),
        migrations.AddField(
            model_name='featuresconfig',
            name='talk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setupWizard.TalkingFeatures'),
        ),
    ]
