# Generated by Django 4.1.6 on 2023-03-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_bookstatus_workspace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
