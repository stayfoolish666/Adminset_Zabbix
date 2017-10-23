# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-26 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, unique=True, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.GenericIPAddressField(verbose_name='\u7ba1\u7406IP')),
                ('other_ip', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5176\u5b83IP')),
                ('asset_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u8d44\u4ea7\u7f16\u53f7')),
                ('asset_type', models.CharField(blank=True, choices=[(b'1', '\u7269\u7406\u673a'), (b'2', '\u865a\u62df\u673a'), (b'3', '\u5bb9\u5668'), (b'4', '\u7f51\u7edc\u8bbe\u5907'), (b'5', '\u5176\u4ed6')], max_length=30, null=True, verbose_name='\u8bbe\u5907\u7c7b\u578b')),
                ('status', models.CharField(blank=True, choices=[(b'1', '\u4f7f\u7528\u4e2d'), (b'2', '\u672a\u4f7f\u7528'), (b'3', '\u6545\u969c'), (b'4', '\u5176\u5b83')], max_length=30, null=True, verbose_name='\u8bbe\u5907\u72b6\u6001')),
                ('os', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('vendor', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u8bbe\u5907\u5382\u5546')),
                ('cpu_model', models.CharField(blank=True, max_length=100, null=True, verbose_name='CPU\u578b\u53f7')),
                ('cpu_num', models.CharField(blank=True, max_length=100, null=True, verbose_name='CPU\u6570\u91cf')),
                ('memory', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u5185\u5b58\u5927\u5c0f')),
                ('disk', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u786c\u76d8\u4fe1\u606f')),
                ('sn', models.CharField(blank=True, max_length=60, verbose_name='SN\u53f7 \u7801')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u6240\u5728\u4f4d\u7f6e')),
                ('memo', models.TextField(blank=True, max_length=200, null=True, verbose_name='\u5907\u6ce8\u4fe1\u606f')),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='\u7ec4\u540d')),
                ('desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u63cf\u8ff0')),
            ],
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='\u673a\u623f\u5730\u5740')),
                ('tel', models.CharField(max_length=30, null=True, verbose_name='\u673a\u623f\u7535\u8bdd')),
                ('contact', models.CharField(max_length=30, null=True, verbose_name='\u5ba2\u6237\u7ecf\u7406')),
                ('contact_phone', models.CharField(max_length=30, null=True, verbose_name='\u79fb\u52a8\u7535\u8bdd')),
                ('jigui', models.CharField(max_length=30, null=True, verbose_name='\u673a\u67dc\u4fe1\u606f')),
                ('ip_range', models.CharField(max_length=30, null=True, verbose_name='IP\u8303\u56f4')),
                ('bandwidth', models.CharField(max_length=30, null=True, verbose_name='\u63a5\u5165\u5e26\u5bbd')),
            ],
            options={
                'verbose_name': '\u6570\u636e\u4e2d\u5fc3',
                'verbose_name_plural': '\u6570\u636e\u4e2d\u5fc3',
            },
        ),
        migrations.CreateModel(
            name='InterFace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('vendor', models.CharField(max_length=30, null=True)),
                ('bandwidth', models.CharField(max_length=30, null=True)),
                ('tel', models.CharField(max_length=30, null=True)),
                ('contact', models.CharField(max_length=30, null=True)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('price', models.IntegerField(verbose_name='\u4ef7\u683c')),
            ],
        ),
        migrations.CreateModel(
            name='IpSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net', models.CharField(max_length=30)),
                ('subnet', models.CharField(max_length=30, null=True)),
                ('describe', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmdb.HostGroup', verbose_name='\u8bbe\u5907\u7ec4'),
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmdb.Idc', verbose_name='\u6240\u5728\u673a\u623f'),
        ),
    ]
