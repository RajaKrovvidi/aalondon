# Generated by Django 2.2.6 on 2019-11-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0005_meeting_day_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='intergroup',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
