# Generated by Django 5.1.4 on 2025-02-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRCodeApp', '0008_alter_qrcode_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='expire_date',
            field=models.DateTimeField(null=True),
        ),
    ]
