# Generated by Django 2.1.8 on 2019-05-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20190508_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='error',
            field=models.TextField(null=True),
        ),
    ]
