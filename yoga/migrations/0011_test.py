# Generated by Django 2.0.7 on 2018-07-05 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0010_auto_20180705_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
            options={
                'default_permissions': 'add',
            },
        ),
    ]
