# Generated by Django 4.1.3 on 2022-11-14 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audios', '0002_alter_music_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='name',
            field=models.TextField(),
        ),
    ]
