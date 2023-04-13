# Generated by Django 4.0.4 on 2023-04-12 18:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('type', models.CharField(choices=[('ON_OFF', 'on_off'), ('TIME', 'time')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('input', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='koelkast.input')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('on_time', models.TimeField(blank=True, null=True)),
                ('off_time', models.TimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('output', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='koelkast.output')),
            ],
        ),
    ]
