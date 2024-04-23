# Generated by Django 5.0.4 on 2024-04-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('brand', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='cloth_images/')),
            ],
            options={
                'verbose_name_plural': 'Clothes',
            },
        ),
    ]