# Generated by Django 3.1 on 2020-09-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
        migrations.AddField(
            model_name='product',
            name='companyname',
            field=models.CharField(default='lakufirma', max_length=50),
        ),
    ]
