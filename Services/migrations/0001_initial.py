# Generated by Django 4.2 on 2023-05-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=50)),
            ],
        ),
    ]
