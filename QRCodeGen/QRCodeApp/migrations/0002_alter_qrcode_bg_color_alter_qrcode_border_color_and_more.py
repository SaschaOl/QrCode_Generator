# Generated by Django 5.1.4 on 2025-02-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRCodeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='bg_color',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='border_color',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='expire_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='qrcode_color',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='qrcode_style',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
