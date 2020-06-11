# Generated by Django 3.0.5 on 2020-05-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_form',
            name='BreakFast',
            field=models.CharField(choices=[('', 'choose....'), ('Dosa', 'Dosa'), ('Pongal', 'Pongal'), ('Masal Puri', 'Masal Puri'), ('Vadai', 'Vada'), ('Itly', 'Itly')], max_length=50),
        ),
        migrations.AlterField(
            model_name='register_form',
            name='Dinner',
            field=models.CharField(choices=[('', 'choose....'), ('Dosa', 'Dosa'), ('Parotta', 'Parotta'), ('Chappathi', 'Chappathi'), ('Naan', 'Naan'), ('Fried_Rice', 'Fried_Rice')], max_length=50),
        ),
        migrations.AlterField(
            model_name='register_form',
            name='Lunch',
            field=models.CharField(choices=[('', 'choose....'), ('Full_Meals', 'Full_Meals'), ('Veg_Biriyani', 'Veg_Biriyani'), ('Chicken_Biriyani', 'Chicken_Biriyani'), ('Parotta', 'Parotta'), ('Noodles', 'Noodles')], max_length=50),
        ),
    ]
