# Generated by Django 4.1.5 on 2023-04-29 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hurryfood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('district', models.CharField(default='Ernakulam', max_length=20)),
                ('city', models.CharField(default='', max_length=60)),
                ('street', models.CharField(default='', max_length=200)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hurryfood.customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='baseorder',
            name='total',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='ct_offer',
        ),
        migrations.RemoveField(
            model_name='dining',
            name='status',
        ),
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(default='pending', max_length=60),
        ),
        migrations.AddField(
            model_name='table',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='baseorder',
            name='discription',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='baseorder',
            name='dish',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='baseorder',
            name='quantity',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='baseorder',
            name='status',
            field=models.CharField(default='pending', max_length=60),
        ),
        migrations.AlterField(
            model_name='table',
            name='number_table',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('RESTAURANT', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hurryfood.restaurants')),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hurryfood.customer')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=30)),
                ('RESTAURANT', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hurryfood.restaurants')),
                ('address', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hurryfood.address')),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hurryfood.customer')),
                ('payment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hurryfood.payment')),
            ],
        ),
    ]
