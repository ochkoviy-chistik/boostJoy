# Generated by Django 4.2.1 on 2023-06-01 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_doc_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='path',
            field=models.CharField(default='', max_length=127),
            preserve_default=False,
        ),
    ]
