# Generated by Django 3.2.12 on 2022-05-26 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_post_posts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='posts',
            new_name='User_posts',
        ),
    ]
