# Generated by Django 4.2.1 on 2023-06-07 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flight',
            options={'ordering': ['date', 'time']},
        ),
        migrations.AlterModelOptions(
            name='passenger',
            options={'verbose_name': 'Passenger', 'verbose_name_plural': 'Passengers'},
        ),
    ]
