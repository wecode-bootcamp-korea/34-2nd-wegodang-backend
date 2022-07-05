# Generated by Django 4.0.5 on 2022-07-05 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45, unique=True)),
                ('first_name', models.CharField(max_length=45, null=True)),
                ('last_name', models.CharField(max_length=45, null=True)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=100, null=True, unique=True)),
                ('kakao_id', models.BigIntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('order_number', models.CharField(max_length=100)),
                ('products_models', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='products.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='users.user')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]