# Generated by Django 3.2 on 2021-04-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinsiderAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='openinsider',
            name='ticker',
            field=models.CharField(default='Null', max_length=50),
        ),
    ]
