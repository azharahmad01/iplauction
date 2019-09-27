# Generated by Django 2.1.7 on 2019-04-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190427_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='email',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='image',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='email',
        ),
        migrations.RemoveField(
            model_name='player',
            name='image',
        ),
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]