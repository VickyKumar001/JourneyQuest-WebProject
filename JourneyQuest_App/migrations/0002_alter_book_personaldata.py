# Generated by Django 5.0.7 on 2024-08-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JourneyQuest_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Personaldata',
            field=models.TextField(max_length=200),
        ),
    ]
