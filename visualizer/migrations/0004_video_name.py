# Generated by Django 2.2.6 on 2019-10-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0003_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default='SOme Data', max_length=100),
            preserve_default=False,
        ),
    ]
