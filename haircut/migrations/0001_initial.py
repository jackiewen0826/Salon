# Generated by Django 2.0.5 on 2018-06-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, max_length=180, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=180, null=True)),
            ],
        ),
    ]