# Generated by Django 4.2.3 on 2023-08-14 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piece', '0003_piece_piece_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='piece_image',
            field=models.ImageField(blank=True, null=True, upload_to='Back/files/pieces'),
        ),
    ]