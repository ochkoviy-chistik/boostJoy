# Generated by Django 4.0.2 on 2023-05-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='static/default_avatar.png', upload_to='media/', verbose_name='Avatar'),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='sb', max_length=30, verbose_name='first name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='sb', max_length=30, verbose_name='last name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=30, unique=True, verbose_name='username'),
            preserve_default=False,
        ),
    ]