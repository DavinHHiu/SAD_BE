# Generated by Django 4.0.1 on 2024-05-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=255)),
                ('payment_method', models.CharField(choices=[('Mono', 'Mono'), ('Card', 'Card'), ('Online Banking', 'Online Banking'), ('COD', 'COD')], default='COD', max_length=255)),
                ('status', models.CharField(choices=[('Processing', 'Processing'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Failed', 'Failed'), ('Refunded', 'Refunded')], default='Processing', max_length=255)),
                ('total_price', models.FloatField()),
            ],
        ),
    ]
