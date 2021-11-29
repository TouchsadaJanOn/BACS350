# Generated by Django 3.2.6 on 2021-10-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_superhero_strength'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='description',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='superhero',
            name='weakness',
            field=models.CharField(default='none', max_length=100),
        ),
    ]