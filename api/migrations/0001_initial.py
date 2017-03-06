# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 15:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('Kienyeji', 'Kienyeji'), ('Kenbrew', 'Kenbrew'), ('Layers', 'Layers'), ('Broilers', 'Broilers')], default='', max_length=100)),
                ('location', models.CharField(choices=[('Mombasa', 'Mombasa'), ('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu')], default='', max_length=100)),
                ('image1', models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/')),
                ('image2', models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/')),
                ('image3', models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
