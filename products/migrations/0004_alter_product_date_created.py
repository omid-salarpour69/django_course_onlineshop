# Generated by Django 5.0.3 on 2024-05-10 16:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
