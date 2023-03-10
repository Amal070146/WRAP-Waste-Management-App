# Generated by Django 4.0.4 on 2023-03-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0004_rename_type_booking_wastetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='address',
            field=models.CharField(default=2115, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=515, verbose_name='N j, Y'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='typeaddress',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
