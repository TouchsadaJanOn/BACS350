# Generated by Django 3.2.6 on 2021-10-24 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0006_alter_article_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='html',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='markdown',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]