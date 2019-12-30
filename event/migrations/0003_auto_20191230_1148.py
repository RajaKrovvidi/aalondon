# Generated by Django 2.2.9 on 2019-12-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20191229_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurringeventparent',
            name='recurring_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recurringeventparent',
            name='recurring_day',
            field=models.IntegerField(blank=True, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], null=True),
        ),
        migrations.AlterField(
            model_name='recurringeventparent',
            name='recurring_month',
            field=models.IntegerField(blank=True, choices=[(0, 'Every Month'), (1, 'Every Second Month'), (2, 'Every Third Month')], null=True),
        ),
    ]
