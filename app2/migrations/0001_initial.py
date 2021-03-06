# Generated by Django 2.2.5 on 2020-02-26 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CASTE_NO', models.IntegerField(blank=True, default=None, null=True)),
                ('CASTE_NAME', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'CASTE',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATEGORY_NO', models.IntegerField(blank=True, default=None, null=True)),
                ('CATEGORY_NAME', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'CATEGORY',
            },
        ),
        migrations.CreateModel(
            name='Designature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DESIGNATURE_NO', models.IntegerField(blank=True, default=None, null=True)),
                ('DESIGNATURE_NAME', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'DESIGNATURE',
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RELIGION_NO', models.IntegerField(blank=True, default=None, null=True)),
                ('RELIGION_NAME', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'RELIGION',
            },
        ),
        migrations.CreateModel(
            name='SuplHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SUPLNO', models.IntegerField(blank=True, default=None, null=True)),
                ('SUPLHEAD_NAME', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'SUPLHEAD',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TITLE_NO', models.IntegerField(blank=True, default=None, null=True)),
                ('TITLE_NAME', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'TITLE',
            },
        ),
        migrations.CreateModel(
            name='TypeTran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TYPETRAN_NO', models.IntegerField(blank=True, default=None, null=True)),
                ('TYPETRAN_NAME', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'TYPETRAN',
            },
        ),
    ]
