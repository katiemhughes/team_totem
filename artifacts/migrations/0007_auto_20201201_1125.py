# Generated by Django 3.1.3 on 2020-12-01 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0006_artifact_discovered_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artifact',
            old_name='artifact_info',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='artifact',
            old_name='artifact_text',
            new_name='text',
        ),
    ]
