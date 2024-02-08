# Generated by Django 4.2.7 on 2024-02-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_lojista_image_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='lojista',
            name='image',
            field=models.ImageField(upload_to='lojistasImages/06_02_2024'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profileImages/06_02_2024'),
        ),
        migrations.AddField(
            model_name='lojista',
            name='categories',
            field=models.ManyToManyField(blank=True, to='account.category'),
        ),
    ]