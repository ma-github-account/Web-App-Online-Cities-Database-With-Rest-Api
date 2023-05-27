# Generated by Django 4.1.4 on 2023-05-27 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_extrainfo_rodzaj'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('capitol', models.TextField(max_length=256)),
                ('population', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='film',
            name='extra_info',
        ),
        migrations.RemoveField(
            model_name='recenzja',
            name='film',
        ),
        migrations.DeleteModel(
            name='Aktor',
        ),
        migrations.DeleteModel(
            name='ExtraInfo',
        ),
        migrations.DeleteModel(
            name='Film',
        ),
        migrations.DeleteModel(
            name='Recenzja',
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='api.country'),
        ),
    ]