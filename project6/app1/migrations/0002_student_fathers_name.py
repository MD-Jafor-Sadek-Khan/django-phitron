# Generated by Django 4.2.4 on 2023-08-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fathers_name',
            field=models.TextField(default='Rahim'),
        ),
    ]
