# Generated by Django 3.1.7 on 2021-07-01 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], default='New', max_length=10),
        ),
    ]
