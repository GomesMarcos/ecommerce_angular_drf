# Generated by Django 3.1.6 on 2021-02-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20210201_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default='', upload_to='', verbose_name='Imagem do produto'),
            preserve_default=False,
        ),
    ]
