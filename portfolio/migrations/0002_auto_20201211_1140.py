# Generated by Django 3.1.4 on 2020-12-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio/static/img/blog', verbose_name='post_image'),
        ),
    ]