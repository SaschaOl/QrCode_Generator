# Generated by Django 5.1.4 on 2025-02-21 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRCodeApp', '0010_remove_qrcode_border_color_and_more'),
        ('UserApp', '0003_alter_profile_subscription_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcode',
            name='logo',
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.profile'),
        ),
    ]
