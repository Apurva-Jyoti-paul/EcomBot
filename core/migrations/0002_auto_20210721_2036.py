# Generated by Django 3.2.5 on 2021-07-21 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='conttype',
            field=models.CharField(blank=True, default='text', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='countrycode',
            field=models.CharField(blank=True, default='91', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='dialcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='source',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
