# Generated by Django 3.0.5 on 2020-07-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='id',
        ),
        migrations.AddField(
            model_name='todo',
            name='work_id',
            field=models.AutoField(default='0', primary_key=True, serialize=False),
        ),
    ]
