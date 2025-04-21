from datetime import timezone

from django.core.validators import MinValueValidator
from django.db import models

class Season(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Country(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Club(models.Model):
    name=models.CharField(max_length=255)
    logo=models.ImageField(upload_to='images/')
    president=models.CharField(max_length=255,blank=True)
    coach=models.CharField(max_length=255)
    found_date=models.DateField()
    country=models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Player(models.Model):
    name=models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    age=models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])
    price=models.FloatField(validators=[MinValueValidator(0)])
    club=models.ForeignKey(Club,on_delete=models.CASCADE)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transfer(models.Model):
    old_club=models.ForeignKey(Club,on_delete=models.CASCADE,related_name='old_club')
    new_club=models.ForeignKey(Club,on_delete=models.CASCADE,related_name='new_club')
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    price=models.FloatField(validators=[MinValueValidator(0)])
    price_tft=models.FloatField(validators=[MinValueValidator(0)])
    created_at=models.DateField()
    date=models.DateField(auto_now_add=True)
    season=models.ForeignKey(Season,on_delete=models.CASCADE)