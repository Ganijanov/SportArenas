# B.B.R
from django.db import models
from django.contrib.auth.models import User

class Viloyat(models.Model):
    nomi = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.nomi


class Shaxar(models.Model):
    nomi = models.CharField(max_length=250)
    viloyat = models.ForeignKey(Viloyat , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nomi



class Arena(models.Model):
    tumon_sh = models.ForeignKey(Shaxar, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=250)
    parking = models.BooleanField(default=False)
    dush = models.BooleanField(default=True)
    orindiq = models.IntegerField()
    bsh_voqti = models.TimeField()
    haqida = models.TextField(null=True)
    tgsh_voqti = models.TimeField()
    tamir = models.DateField()
    maydon = models.FloatField()

    def __str__(self) -> str:
        return self.nomi


class Sport(models.Model):
    nomi = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='Sport/')
    bio = models.CharField(max_length=255, default="Mavjud emas")
    arena = models.ForeignKey(Arena, on_delete=models.CASCADE, related_name='arena')

    def __str__(self) -> str:
        return self.nomi


class Rasm(models.Model):
    arena = models.ForeignKey(Arena,on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='arena/')

    def __str__(self) -> str:
        return self.arena.nomi

class Murabbiy(models.Model):
    img = models.ImageField(upload_to='Murabbi/')
    name = models.CharField( max_length=250)
    lname = models.CharField( max_length=250)
    insta = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='murabbiy')

    def __str__(self) -> str:
        return self.name
    
