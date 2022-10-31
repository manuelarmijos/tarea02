# Generated by Django 4.1.2 on 2022-10-31 02:53

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_homepage_options_remove_homepage_body_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={},
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_title',
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
