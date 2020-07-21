# Generated by Django 3.0.5 on 2020-07-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=50)),
                ('due_date', models.DateField()),
                ('desc', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
