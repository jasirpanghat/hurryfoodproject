# Generated by Django 4.2 on 2023-05-12 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hurryfood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dining',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 12, 15, 11, 51, 752531)),
        ),
    ]
