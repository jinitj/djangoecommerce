# Generated by Django 2.2.5 on 2019-10-22 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_identifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Customer'),
        ),
    ]
