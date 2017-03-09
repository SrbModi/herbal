# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrder',
            fields=[
                ('order_date', models.DateField(auto_now=True)),
                ('txnid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('hash', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_name', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_street_address', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_country', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_state', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_pincode', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_mobile', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_email', models.CharField(blank=True, max_length=500, null=True)),
                ('shipping_name', models.CharField(blank=True, max_length=500, null=True)),
                ('shipping_street_address', models.CharField(blank=True, max_length=500, null=True)),
                ('shipping_country', models.CharField(blank=True, max_length=500, null=True)),
                ('shipping_state', models.CharField(blank=True, max_length=500, null=True)),
                ('shipping_city', models.CharField(blank=True, max_length=500, null=True)),
                ('shipping_pincode', models.CharField(blank=True, max_length=500, null=True)),
                ('shipping_mobile', models.CharField(blank=True, max_length=500, null=True)),
                ('shipping_rate', models.FloatField(default=0.0)),
                ('status', models.CharField(blank=True, max_length=500, null=True)),
                ('shipping_email', models.CharField(blank=True, max_length=500, null=True)),
                ('payment_method', models.CharField(max_length=1000, verbose_name='Payment-method')),
                ('is_paid', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('is_accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='order_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.SmallIntegerField()),
                ('prod_name', models.CharField(max_length=15)),
                ('prod_id', models.IntegerField()),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('qty', models.SmallIntegerField(default=1)),
                ('offer', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order_delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('order_id', models.SmallIntegerField()),
                ('contact', models.BigIntegerField(default=0)),
                ('email', models.CharField(max_length=100, null=True, unique=True)),
                ('address', models.CharField(max_length=256, null=True)),
                ('landmark', models.CharField(max_length=256, null=True)),
                ('city', models.CharField(max_length=256, null=True)),
                ('state', models.CharField(max_length=256, null=True)),
                ('pincode', models.SmallIntegerField(default=492010)),
            ],
        ),
    ]
