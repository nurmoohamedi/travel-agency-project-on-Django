from django.db import models


class Member(models.Model):
    name = models.CharField('team member', max_length=50)
    number = models.IntegerField('number')
    email = models.CharField('team member', max_length=50)
    position = models.CharField('member position', max_length=50)
    bdate = models.DateTimeField('birth date')

    def __str__(self):
        return self.name


class Tour(models.Model):
    id = models.IntegerField('id', primary_key=True)
    name = models.CharField('tour_name', max_length=60)
    description = models.TextField('tour_name')
    started = models.DateTimeField('started date')
    duration = models.IntegerField('tour_duration')
    price = models.IntegerField('tour price')
    image = models.FileField(upload_to='tours/')

    def __str__(self):
        return self.name