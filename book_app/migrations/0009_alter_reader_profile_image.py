# Generated by Django 4.1.1 on 2022-09-16 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0008_alter_reader_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader_profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]