# Generated by Django 4.0.2 on 2023-05-30 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='media/default_images/default_avatar.png', upload_to='media/', verbose_name='Avatar'),
        ),
    ]
