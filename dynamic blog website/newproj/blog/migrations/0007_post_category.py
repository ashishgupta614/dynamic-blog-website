# Generated by Django 5.1b1 on 2024-07-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
