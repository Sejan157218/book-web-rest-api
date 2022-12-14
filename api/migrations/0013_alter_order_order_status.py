# Generated by Django 3.2 on 2022-10-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('On the way', 'On the way'), ('Order Received', 'Order Received'), ('Order Canceled', 'Order Canceled'), ('Order Completed', 'Order Completed'), ('Order Processing', 'Order Processing')], default='Order Received', max_length=100),
        ),
    ]
