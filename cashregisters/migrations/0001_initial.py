# Generated by Django 5.0.6 on 2024-10-19 13:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('saldo_inicial', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_cierre', models.DateTimeField(auto_now_add=True)),
                ('user_made', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_user_made', to=settings.AUTH_USER_MODEL, verbose_name='Por')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(max_length=255)),
                ('tipo_pago', models.CharField(verbose_name=100)),
                ('caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos', to='cashregisters.caja')),
                ('user_made', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_user_made', to=settings.AUTH_USER_MODEL, verbose_name='Por')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Arqueo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('observaciones', models.CharField(max_length=255)),
                ('saldo_final', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user_made', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_user_made', to=settings.AUTH_USER_MODEL, verbose_name='Por')),
                ('caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arqueos', to='cashregisters.caja')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashregisters.usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
