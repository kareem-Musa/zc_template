# Generated by Django 3.1.6 on 2021-02-17 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_locality'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='الوحدة الادارية')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.locality', verbose_name='المحلية')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.state', verbose_name='الولاية')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='المدينة')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.locality', verbose_name='المحلية')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.state', verbose_name='الولاية')),
                ('unity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.unity', verbose_name='الوحدة الادارية')),
            ],
        ),
    ]