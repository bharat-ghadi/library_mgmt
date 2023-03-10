# Generated by Django 4.1.6 on 2023-03-09 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_stat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('contact', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=300)),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.membership')),
            ],
        ),
    ]
