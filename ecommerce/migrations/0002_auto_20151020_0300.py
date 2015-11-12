# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=0, max_digits=24, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(related_name='children', blank=True, to='ecommerce.Category', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
