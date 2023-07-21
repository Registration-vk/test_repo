# Generated by Django 4.2.2 on 2023-07-21 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_projects', '0004_alter_videoexerciserec_videofield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagecarnumdetect',
            old_name='ImgCarNumDetect',
            new_name='InputImage',
        ),
        migrations.RenameField(
            model_name='imagesexagedetect',
            old_name='ImgSexAgeDetect',
            new_name='InputImage',
        ),
        migrations.RenameField(
            model_name='videoexerciserec',
            old_name='VideoField',
            new_name='InputVideo',
        ),
    ]
