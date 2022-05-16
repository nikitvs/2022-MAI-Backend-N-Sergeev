# Generated by Django 4.0 on 2022-05-15 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=1)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='category.category')),
            ],
        ),
    ]
