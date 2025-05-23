# Generated by Django 5.2 on 2025-05-08 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_auto_parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='img/cats/')),
                ('self_url', models.CharField(max_length=255)),
                ('leaf', models.BooleanField(default=False)),
                ('recommendedQuantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque_id', models.IntegerField()),
                ('marque', models.CharField(max_length=100)),
                ('model_id', models.IntegerField()),
                ('model_name', models.CharField(max_length=150)),
                ('vehicle_id', models.IntegerField()),
                ('vehicle_name', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('self_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory_auto_parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='img/cats/')),
                ('self_url', models.CharField(max_length=255)),
                ('leaf', models.BooleanField(default=False)),
                ('recommendedQuantity', models.IntegerField(default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='carparts.category_auto_parts')),
            ],
        ),
    ]
