# Generated by Django 3.1.7 on 2021-05-02 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_contactformmessage_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=10),
        ),
    ]
