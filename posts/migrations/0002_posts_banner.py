# Generated by Django 5.1.5 on 2025-01-30 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='banner',
            field=models.ImageField(default='fallback.png', upload_to=''),
        ),
    ]
