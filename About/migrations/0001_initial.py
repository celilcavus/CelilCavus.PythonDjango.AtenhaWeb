# Generated by Django 4.2 on 2023-05-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(default='', max_length=500)),
            ],
        ),
    ]
