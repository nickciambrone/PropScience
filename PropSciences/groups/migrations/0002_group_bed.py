# Generated by Django 2.2.1 on 2019-06-14 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='bed',
            field=models.CharField(default=3, max_length=255),
            preserve_default=False,
        ),
    ]