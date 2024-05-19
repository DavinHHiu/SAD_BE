# Generated by Django 4.0.1 on 2024-05-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('shipping_method', models.CharField(choices=[('Standard', 'Standard'), ('Express', 'Express'), ('Super Express', 'Super Express')], default='Standard', max_length=255)),
                ('shipping_status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('In transit', 'In transit'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Returned', 'Returned')], default='Processing', max_length=255)),
                ('estimated_delivery_date', models.DateField()),
                ('shipping_fee', models.FloatField(default=2.99)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
