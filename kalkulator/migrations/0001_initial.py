# Generated by Django 4.1.1 on 2022-09-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rankMobileLegends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rankml', models.CharField(max_length=100)),
                ('divisirankml', models.CharField(max_length=100)),
                ('subrankml', models.CharField(max_length=100)),
                ('harga', models.IntegerField()),
                ('urutan', models.IntegerField()),
            ],
        ),
    ]
