# Generated by Django 4.1 on 2022-09-04 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_rename_create_at_comment_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
