# Generated by Django 3.2.7 on 2021-09-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20210904_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='no photo', upload_to='photos'),
        ),
    ]