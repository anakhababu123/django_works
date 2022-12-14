# Generated by Django 4.1.1 on 2022-10-08 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=150, null=True)),
                ('price', models.PositiveIntegerField(default=1000)),
                ('bands', models.CharField(choices=[('4G', '4G'), ('5G', '5G'), ('3G', '3G')], default='5G', max_length=150)),
                ('display', models.CharField(choices=[('LED', 'LED'), ('AMLED', 'AMLED'), ('SMLED', 'SMLED')], default='LED', max_length=50)),
            ],
        ),
    ]
