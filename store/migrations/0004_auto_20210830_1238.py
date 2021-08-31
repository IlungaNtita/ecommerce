# Generated by Django 2.2.13 on 2021-08-30 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210830_1111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
