# Generated by Django 3.0.5 on 2020-06-04 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_auto_20200604_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_form',
            name='BreakFast',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='register_form',
            name='Dinner',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='register_form',
            name='Lunch',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
