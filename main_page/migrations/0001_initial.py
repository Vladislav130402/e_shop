# Generated by Django 4.2.1 on 2023-05-30 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('added_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('product_description', models.CharField(max_length=240)),
                ('product_price', models.FloatField()),
                ('product_amount', models.IntegerField()),
                ('product_images', models.ImageField(upload_to='media')),
                ('product_added_data', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.category')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('user_cart_amount', models.IntegerField()),
                ('cart_added_data', models.DateTimeField(auto_now_add=True)),
                ('user_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.products')),
            ],
        ),
    ]