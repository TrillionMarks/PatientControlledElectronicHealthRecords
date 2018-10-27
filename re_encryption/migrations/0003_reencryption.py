# Generated by Django 2.1.2 on 2018-10-27 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('re_encryption', '0002_auto_20181025_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReEncryption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verifying_key', models.CharField(blank=True, max_length=200, null=True)),
                ('recepient_id', models.IntegerField()),
                ('records_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='re_encryption.RecordsSet')),
            ],
        ),
    ]
