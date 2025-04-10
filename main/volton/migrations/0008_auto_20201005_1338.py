# Generated by Django 3.0.5 on 2020-10-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volton', '0007_auto_20201005_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='products',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='volton.Keywords', verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='products',
            name='titlesite',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Title'),
        ),
        migrations.AddField(
            model_name='productstr',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='productstr',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='volton.KeywordsTR', verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='productstr',
            name='titlesite',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Site Title'),
        ),
    ]
