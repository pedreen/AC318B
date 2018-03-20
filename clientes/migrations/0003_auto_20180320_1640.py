# Generated by Django 2.0.3 on 2018-03-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20180320_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=30)),
                ('Senha', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Nome', models.CharField(max_length=30)),
                ('Endereco', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Celular', models.CharField(max_length=30)),
                ('AvaliacaoEmpresa', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
