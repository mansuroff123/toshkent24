# Generated by Django 4.0.4 on 2022-05-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
