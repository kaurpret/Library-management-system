# Generated by Django 3.2.12 on 2022-07-31 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sec_app1', '0023_auto_20220731_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='return_book',
            name='user_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sec_app1.created'),
        ),
    ]
