# Generated by Django 5.0.1 on 2024-01-16 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_categorymodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog.categorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='goods_images')),
                ('short_description', models.CharField(blank=True, max_length=150, null=True)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.goodmodel')),
            ],
        ),
    ]