# Generated by Django 3.2.9 on 2021-11-12 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_platorms'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='platorm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.platorm'),
        ),
    ]
