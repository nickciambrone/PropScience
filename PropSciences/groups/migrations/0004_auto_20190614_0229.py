# Generated by Django 2.2.1 on 2019-06-14 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20190614_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='bath',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='group',
            name='bed',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='housepics', verbose_name='Image')),
                ('group', models.ForeignKey(default=None, on_delete='cascade', to='groups.Group')),
            ],
        ),
    ]