from django.db import models
from django.core.exceptions import ValidationError


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class CommandCategory(models.Model):
    
    class Meta:
        verbose_name_plural = "Command Categories"

    COLORS = (
        ("red", "Red"),
        ("blue", "Blue"),
        ("green", "Green"),
        ("yellow", "Yellow"),
        ("violet", "Violet"),
        ("orange", "Orange"),
        ("black", "Black"),
        ("gray", "Gray"),
    )

    identifier = models.CharField(null=False, blank=False, unique=True, max_length=20)

    display_order = models.IntegerField(blank=False,null=False,default=0)

    button_color = models.CharField(choices=COLORS,max_length=32,null=False,blank=False, default="blue")

    def __str__(self):
        return self.identifier + ": " + self.button_color


class ParrotCommand(models.Model):

    class Meta:
        verbose_name_plural = "Parrot Commands"

    TAG_CHOICES = (
        ("P_M", "Parrot Movement"),
        ("P_V", "Parrot Voice"),
    )

    name = models.CharField(max_length=40,null=False,blank=False)
    title = models.CharField(max_length=40,null=False,blank=False)
    category = models.ForeignKey(CommandCategory, on_delete= models.CASCADE)
    tag = models.CharField(choices=TAG_CHOICES,max_length=4,null=False,blank=False)
    priority = models.IntegerField(blank=False,null=False,default=0)
    arg = models.IntegerField(unique=True,blank=False,null=False)
    voice_file_name = models.CharField(max_length=512, blank=True, default='')
    perform_time = models.IntegerField(default=5) #in second
    parrot_0 = models.BooleanField(default=True, null=False)
    parrot_1 = models.BooleanField(default=True, null=False)
    choices_tuple = (
        ('💃',"💃"), ("'😃🙂'","'😃🙂'"),
        ("'😛😝'","'😛😝'"), ("'😛'","'😛'"), ("'😝'","'😝'"),
        ("'😃'","'😃'"),("'🙂'","'🙂'")
    )

    interface_button_emoji = models.CharField(max_length=25,choices=choices_tuple)


    def is_voice(self):
        return self.tag == "P_V"

    def __str__(self):
        return self.tag + ": " + self.name

class BlueParrotCommand(ParrotCommand):
    class Meta:
        proxy = True

class RedParrotCommand(ParrotCommand):
    class Meta:
        proxy = True


class CommandConfig(models.Model):

    class Meta:
        verbose_name_plural = "Commands Config"

    def clean(self):
        validate_only_one_instance(self)

    red_parrot_voice_path_prefix = models.CharField(max_length= 256, blank=True, default= "./")
    red_parrot_voice_path_postfix = models.CharField(max_length= 256, blank=True, default= ".wav")

    blue_parrot_voice_path_prefix = models.CharField(max_length= 256, blank=True, default= "./")
    blue_parrot_voice_path_postfix = models.CharField(max_length= 256, blank=True, default= ".wav")

    @staticmethod
    def get():
        try:
            return CommandConfig.objects.all()[0]
        except IndexError:
            return CommandConfig.objects.create()

    def __str__(self):
        return 'Command Config'