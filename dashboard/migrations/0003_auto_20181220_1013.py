# Generated by Django 2.1 on 2018-12-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_memberinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberinfo',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
