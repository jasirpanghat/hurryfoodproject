# Generated by Django 4.1.5 on 2023-05-02 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hurryfood', '0005_remove_baseorder_restaurant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseorder',
            name='RESTAURANT',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hurryfood.restaurants'),
        ),
        migrations.AddField(
            model_name='baseorder',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hurryfood.customer'),
        ),
    ]
