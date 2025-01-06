# Generated by Django 3.2.12 on 2025-01-05 16:21

from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import now


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_order_assigned_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='created_at',
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='menu_item',
            field=models.ForeignKey(
                default=None,  # Replace `None` with a valid MenuItem ID if required
                on_delete=django.db.models.deletion.CASCADE,
                to='restaurant.menuitem'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='receipt',
            name='generated_at',
            field=models.DateTimeField(default=now),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(
                choices=[
                    ('Pending', 'Pending'),
                    ('Completed', 'Completed'),
                    ('Cancelled', 'Cancelled')
                ],
                default='Pending',
                max_length=20
            ),
        ),
    ]
