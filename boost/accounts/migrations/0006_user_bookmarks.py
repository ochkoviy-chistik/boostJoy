# Generated by Django 4.2.1 on 2023-06-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_doc_comments'),
        ('accounts', '0005_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(to='app.doc'),
        ),
    ]
