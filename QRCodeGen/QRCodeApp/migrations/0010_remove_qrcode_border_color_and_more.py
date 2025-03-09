# Generated by Django 5.1.4 on 2025-02-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRCodeApp', '0009_alter_qrcode_expire_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcode',
            name='border_color',
        ),
        migrations.RemoveField(
            model_name='qrcode',
            name='qrcode_style',
        ),
        migrations.AddField(
            model_name='qrcode',
            name='logo',
            field=models.ImageField(null=True, upload_to='', verbose_name='logos/'),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='expire_date',
            field=models.DateTimeField(),
        ),
    ]
