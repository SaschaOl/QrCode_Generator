# Generated by Django 5.1.4 on 2025-02-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRCodeApp', '0004_alter_qrcode_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
