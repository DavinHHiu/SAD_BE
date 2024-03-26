# Generated by Django 5.0.3 on 2024-03-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='book_covers/')),
            ],
        ),
    ]
