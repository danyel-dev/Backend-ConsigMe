# Generated by Django 4.2.7 on 2024-02-19 11:31

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('account', '0021_category_alter_lojista_image_alter_profile_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lojista',
            name='categories',
        ),
        migrations.AddField(
            model_name='lojista',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='lojista',
            name='image',
            field=models.ImageField(upload_to='lojistasImages/19_02_2024'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profileImages/19_02_2024'),
        ),
    ]
