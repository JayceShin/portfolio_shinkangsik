# Generated by Django 3.0.2 on 2020-01-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inception', '0002_auto_20200104_0510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.TextField(null=True, verbose_name='number')),
                ('oper', models.TextField(null=True, verbose_name='operator')),
                ('res', models.TextField(null=True, verbose_name='result')),
            ],
        ),
    ]
