# Generated by Django 5.1.4 on 2025-02-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_alter_profile_subscription_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subscription',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='subscription_expire_date',
            field=models.DateTimeField(null=True),
        ),
    ]
