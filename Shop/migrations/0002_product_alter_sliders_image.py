# Generated by Django 4.2.2 on 2023-11-04 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='uploads/products/product1.jpg', upload_to='uploads/products')),
                ('name', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='sliders',
            name='image',
            field=models.ImageField(default='uploads/sliders/person-1.jpg', upload_to='uploads/sliders'),
        ),
    ]
