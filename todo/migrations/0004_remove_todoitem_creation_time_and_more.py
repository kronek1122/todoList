# Generated by Django 4.1.1 on 2022-11-08 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_text_todoitem_todo_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='creation_time',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='piority',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='user',
        ),
    ]
