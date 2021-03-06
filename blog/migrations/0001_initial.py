# Generated by Django 3.1.2 on 2021-01-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=300)),
                ('date', models.DateField(blank=True)),
                ('urls', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='portfolio/images/')),
            ],
        ),
        migrations.CreateModel(
            name='MyTunes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('sound_file', models.FileField(blank=True, upload_to='static/music/')),
            ],
        ),
        migrations.CreateModel(
            name='Trails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('urls', models.URLField(blank=True)),
            ],
        ),
    ]
