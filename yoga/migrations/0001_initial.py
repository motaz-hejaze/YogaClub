# Generated by Django 2.0.7 on 2018-07-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=50)),
                ('paragraph1', models.TextField()),
                ('title2', models.CharField(max_length=50)),
                ('paragraph2', models.TextField()),
                ('title3', models.CharField(max_length=50)),
                ('paragraph3', models.TextField()),
                ('title4', models.CharField(max_length=50)),
                ('paragraph4', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=50)),
                ('paragraph1', models.TextField()),
                ('MWF1', models.CharField(max_length=20)),
                ('TTHS1', models.CharField(max_length=20)),
                ('title2', models.CharField(max_length=50)),
                ('paragraph2', models.TextField()),
                ('MWF2', models.CharField(max_length=20)),
                ('TTHS2', models.CharField(max_length=20)),
                ('title3', models.CharField(max_length=50)),
                ('paragraph3', models.TextField()),
                ('MWF3', models.CharField(max_length=20)),
                ('TTHS3', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('facebook', models.URLField(max_length=50)),
                ('twitter', models.URLField(max_length=50)),
                ('pinterest', models.URLField(max_length=50)),
                ('google', models.URLField(max_length=50)),
                ('background', models.ImageField(upload_to='website_images')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='instructors_images')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='posts_images')),
                ('date', models.DateField()),
                ('paragraph', models.TextField()),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]