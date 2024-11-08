# Generated by Django 5.1 on 2024-10-31 11:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RentVehichle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownername', models.CharField(max_length=200)),
                ('shop_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200, null=True)),
                ('whatsapp_no', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('hdstatus', models.CharField(max_length=200, null=True)),
                ('shop_registration', models.FileField(default='', upload_to='vehichle registration')),
                ('shop_photo', models.ImageField(default='', upload_to='vehichle images')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
