# Generated by Django 3.0.5 on 2020-10-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volton', '0002_bros_brosen_certifica_certificaen_iletisim_klavuz_klavuzen_products_productstr_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstr',
            name='category',
            field=models.CharField(choices=[('MCCB', 'MCCB'), ('CONTACTOR', 'CONTACTOR'), ('MMS', 'MMS'), ('MSB', 'MSB'), ('SPD', 'SPD'), ('ACB', 'ACB'), ('EMPR', 'EMPR')], default='MCCB', max_length=500, verbose_name='Kategori Seçiniz'),
        ),
    ]
