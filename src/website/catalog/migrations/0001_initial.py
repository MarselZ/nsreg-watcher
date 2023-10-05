# Generated by Django 4.1.7 on 2023-10-05 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParseHistory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registrator',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('nic_handle1', models.TextField()),
                ('nic_handle2', models.TextField()),
                ('website', models.TextField()),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('domain', models.CharField(choices=[('ru', 'Ru')], max_length=10)),
                ('price_reg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_prolong', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_change', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.parsehistory')),
                ('registrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.registrator')),
            ],
        ),
        migrations.CreateModel(
            name='Parser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('contributor_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('registrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.registrator')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParseError',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('parse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.parsehistory')),
                ('parser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.parser')),
            ],
        ),
    ]
