# Generated by Django 3.1.2 on 2020-10-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='iconn',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
