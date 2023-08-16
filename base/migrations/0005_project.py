# Generated by Django 4.2.4 on 2023-08-15 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_internship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('certification_link', models.URLField(default='www.google.com')),
            ],
        ),
    ]
