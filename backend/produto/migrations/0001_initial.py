# Generated by Django 3.1.6 on 2021-02-02 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=99, verbose_name='Preço do produto')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('categoria', models.CharField(max_length=50, verbose_name='Categoria')),
                ('preco_oferta', models.DecimalField(decimal_places=2, default=0.0, max_digits=99, verbose_name='Preço do produto em oferta')),
                ('previsão_entrega', models.SmallIntegerField(verbose_name='Previsão da entrega em dias')),
                ('data_prevista_entrega', models.DateField(verbose_name='Data prevista para entrega')),
                ('sku', models.CharField(max_length=50)),
                ('quantidade_estoque', models.IntegerField(default=0, verbose_name='Quantidade em estoque')),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
            },
        ),
    ]
