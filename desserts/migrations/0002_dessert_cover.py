# Generated by Django 4.0.4 on 2022-12-30 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desserts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dessert',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]