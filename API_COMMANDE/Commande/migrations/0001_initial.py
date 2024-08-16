# Generated by Django 5.1 on 2024-08-16 08:21

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Commandes',
            fields=[
                ('createdAt', models.DateField(default=datetime.date.today)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customerId', models.IntegerField(default=1)),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Commande.produits')),
            ],
        ),
    ]
