# Generated by Django 3.1.7 on 2021-05-01 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210501_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='message',
            field=models.CharField(max_length=255),
        ),
    ]