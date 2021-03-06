# Generated by Django 3.1.6 on 2021-02-02 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome do produto')),
                ('preco', models.DecimalField(decimal_places=2, editable=False, max_digits=99, verbose_name='preço do produto')),
                ('descricao', models.TextField(verbose_name='descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data da venda')),
                ('total', models.DecimalField(decimal_places=2, max_digits=99, verbose_name='Valor total da venda')),
                ('produtos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produto.produto')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]
