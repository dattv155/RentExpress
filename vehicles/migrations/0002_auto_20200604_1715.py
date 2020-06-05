# Generated by Django 3.0.6 on 2020-06-04 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='productVendor',
            new_name='manufacturer',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='rate',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='rentPrice',
            new_name='rent_price',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicleName',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
    ]