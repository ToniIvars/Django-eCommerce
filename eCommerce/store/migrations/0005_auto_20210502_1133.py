# Generated by Django 3.1.7 on 2021-05-02 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='state',
        ),
    ]
