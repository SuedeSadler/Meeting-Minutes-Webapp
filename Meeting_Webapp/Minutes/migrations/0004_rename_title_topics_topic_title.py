# Generated by Django 4.0.6 on 2022-08-11 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Minutes', '0003_alter_post_atendees_alter_topics_actioned_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topics',
            old_name='Title',
            new_name='Topic_Title',
        ),
    ]