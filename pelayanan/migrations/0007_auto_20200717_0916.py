# Generated by Django 3.0.8 on 2020-07-17 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
        ('accounts', '0003_auto_20200714_1555'),
        ('pelayanan', '0006_auto_20200717_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pengaduans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keluhan', models.TextField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('selesai', models.BooleanField(null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Client')),
                ('kategori_penanganan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.KategoriPenanganan')),
                ('kategori_pengaduan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.KategoriPengaduan')),
            ],
        ),
        migrations.AlterField(
            model_name='respons',
            name='pengaduan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pelayanan.Pengaduans'),
        ),
    ]
