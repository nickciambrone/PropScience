# Generated by Django 2.2.1 on 2019-06-14 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, upload_to='housepics'),
        ),
    ]
