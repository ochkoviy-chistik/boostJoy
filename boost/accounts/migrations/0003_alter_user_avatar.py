# Generated by Django 4.0.2 on 2023-05-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_avatar_user_first_name_user_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='media/default_images/default_avatar.png', upload_to='media/', verbose_name='Avatar'),
        ),
    ]
