# Generated by Django 4.1 on 2023-03-19 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsApp', '0003_dailygoal_mailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailygoal',
            name='goal',
            field=models.IntegerField(default=0),
        ),
    ]