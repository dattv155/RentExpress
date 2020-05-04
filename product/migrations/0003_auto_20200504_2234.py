# Generated by Django 3.0.6 on 2020-05-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='productlines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productLineName', models.CharField(default='', max_length=100)),
                ('slug', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(default='', max_length=100)),
                ('productVendor', models.CharField(default='', max_length=100)),
                ('productDescription', models.TextField(default='')),
                ('quantityInStock', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='Pictures')),
                ('rentPrice', models.IntegerField(default=0)),
                ('rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='promotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promoCode', models.CharField(default='', max_length=15)),
                ('discount', models.IntegerField(default=0)),
                ('startTime', models.DateTimeField(blank=True, null=True)),
                ('endTime', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='variations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('sale_price', models.IntegerField(default=0)),
                ('inStock', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='product',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]