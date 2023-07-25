# Generated by Django 4.2.2 on 2023-07-25 16:46

from django.db import migrations, models
import my_projects.validators


class Migration(migrations.Migration):

    dependencies = [
        ('my_projects', '0005_rename_imgcarnumdetect_imagecarnumdetect_inputimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoexerciserec',
            name='InputVideo',
            field=models.FileField(null=True, upload_to='videos/', validators=[my_projects.validators.validate_file_size, my_projects.validators.validate_min_number_of_frames], verbose_name=''),
        ),
    ]
