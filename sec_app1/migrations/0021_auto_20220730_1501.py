# Generated by Django 3.2.12 on 2022-07-30 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sec_app1', '0020_rename_create_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('book_id', models.IntegerField()),
                ('book_category', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('Issued', 'Issued'), ('Not-Issued', 'Not-Issued')], max_length=100)),
                ('user_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sec_app1.created')),
            ],
        ),
        migrations.AlterField(
            model_name='issue_book',
            name='user_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sec_app1.created'),
        ),
        migrations.DeleteModel(
            name='add_books',
        ),
    ]
