# Generated by Django 4.2.7 on 2023-12-09 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_list',
        ),
        migrations.DeleteModel(
            name='TaskList',
        ),
    ]
