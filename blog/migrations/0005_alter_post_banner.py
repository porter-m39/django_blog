# Generated by Django 5.1.4 on 2025-01-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
