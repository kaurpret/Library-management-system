# Generated by Django 3.2.12 on 2022-07-30 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sec_app1', '0008_auto_20220730_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_books',
            name='user_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sec_app1.sign'),
        ),
        migrations.AlterField(
            model_name='add_students',
            name='user_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sec_app1.sign'),
        ),
        migrations.AlterField(
            model_name='issue_book',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sec_app1.sign'),
        ),
        migrations.AlterField(
            model_name='return_book',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sec_app1.sign'),
        ),
    ]
