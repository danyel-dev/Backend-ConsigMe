# Generated by Django 4.2.7 on 2023-12-27 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_profile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profileImages/27_12_2023'),
        ),
    ]