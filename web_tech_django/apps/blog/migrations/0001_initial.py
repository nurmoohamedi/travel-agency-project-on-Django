# Generated by Django 3.2.8 on 2021-12-05 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('place', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='team member')),
                ('number', models.IntegerField(verbose_name='number')),
                ('email', models.CharField(max_length=50, verbose_name='team member')),
                ('position', models.CharField(max_length=50, verbose_name='member position')),
                ('bdate', models.DateTimeField(verbose_name='birth date')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Tour name')),
                ('description', models.TextField(verbose_name='Tour description')),
                ('started', models.DateTimeField(verbose_name='Started date')),
                ('duration', models.IntegerField(verbose_name='Tour duration')),
                ('price', models.IntegerField(verbose_name='Tour price')),
                ('image', models.ImageField(upload_to='tours/', verbose_name='Tour image')),
            ],
        ),
        migrations.CreateModel(
            name='OrderTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.customer')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tour')),
            ],
        ),
    ]
