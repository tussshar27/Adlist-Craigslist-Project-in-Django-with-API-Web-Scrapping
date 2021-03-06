# Generated by Django 3.1.6 on 2021-05-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20210530_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
