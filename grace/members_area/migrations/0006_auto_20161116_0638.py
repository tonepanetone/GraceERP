# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members_area', '0005_auto_20161116_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(blank=True, max_length=75, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Telefone'),
        ),
    ]
