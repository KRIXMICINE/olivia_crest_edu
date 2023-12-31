# Generated by Django 4.2.6 on 2023-10-14 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_testimony_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_body', models.TextField(max_length=500, null=True)),
                ('service_name', models.CharField(max_length=50, null=True)),
                ('service_avatar', models.ImageField(null=True, upload_to='photos/services')),
            ],
        ),
        migrations.RemoveField(
            model_name='about',
            name='services_avatar',
        ),
        migrations.RemoveField(
            model_name='about',
            name='sevice_body',
        ),
        migrations.RemoveField(
            model_name='about',
            name='sevice_name',
        ),
        migrations.AddField(
            model_name='about',
            name='note',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
