# Generated by Django 3.2.6 on 2021-10-24 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0004_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='html',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='article',
            name='markdown',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
