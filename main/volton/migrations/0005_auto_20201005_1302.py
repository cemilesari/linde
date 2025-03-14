# Generated by Django 3.0.5 on 2020-10-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volton', '0004_auto_20201003_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Keyword')),
            ],
            options={
                'verbose_name': 'EN KeyWords',
                'verbose_name_plural': 'EN Keywords',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='KeywordsTR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Keyword')),
            ],
            options={
                'verbose_name': 'TR KeyWords',
                'verbose_name_plural': 'TR Keywords',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='blogtr',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Meta Açıklama'),
        ),
        migrations.AddField(
            model_name='blog',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='volton.Keywords', verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='blogtr',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='volton.KeywordsTR', verbose_name='Keywords'),
        ),
    ]
