# Generated by Django 4.1 on 2023-03-19 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dailyGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(default='Sunday', max_length=30)),
                ('Month', models.CharField(default='March', max_length=30)),
                ('Year', models.CharField(default='2023', max_length=30)),
            ],
        ),
    ]
