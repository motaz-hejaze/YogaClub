# Generated by Django 2.0.7 on 2018-07-05 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0009_auto_20180705_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'default_permissions': 'change'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
