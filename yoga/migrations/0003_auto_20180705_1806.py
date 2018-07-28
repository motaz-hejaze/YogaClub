# Generated by Django 2.0.7 on 2018-07-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0002_instructor_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='order',
        ),
        migrations.AddField(
            model_name='instructor',
            name='position',
            field=models.CharField(choices=[('r', 'right'), ('l', 'left')], default='l', max_length=5),
        ),
    ]