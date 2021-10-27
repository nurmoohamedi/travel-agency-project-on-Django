from django.db import models


class Member(models.Model):
    name = models.CharField('team member', max_length=50)
    number = models.IntegerField('number')
    email = models.CharField('team member', max_length=50)
    position = models.CharField('member position', max_length=50)
    bdate = models.DateTimeField('birth date')

    def __str__(self):
        return self.name