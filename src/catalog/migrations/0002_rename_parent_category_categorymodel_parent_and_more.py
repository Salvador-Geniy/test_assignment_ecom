# Generated by Django 5.0.1 on 2024-01-16 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='parent_category',
            new_name='parent',
        ),
        migrations.AlterUniqueTogether(
            name='categorymodel',
            unique_together={('parent', 'name')},
        ),
    ]
