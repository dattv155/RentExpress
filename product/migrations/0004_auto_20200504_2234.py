# Generated by Django 3.0.6 on 2020-05-04 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20200504_2234'),
        ('product', '0003_auto_20200504_2234'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Variation',
        ),
        migrations.AddField(
            model_name='variations',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products'),
        ),
        migrations.AddField(
            model_name='products',
            name='productLine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productlines'),
        ),
    ]