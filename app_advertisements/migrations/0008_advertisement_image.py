# Generated by Django 4.2.5 on 2023-09-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0007_remove_advertisement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='/static/img/pict.png', upload_to='advertisements/', verbose_name='Изображение'),
        ),
    ]
