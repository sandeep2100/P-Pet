# Generated by Django 4.2.6 on 2023-10-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('pet_name', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
            ],
        ),
    ]
