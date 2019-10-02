# Generated by Django 2.1 on 2019-10-01 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0006_delete_ipstune'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPSTune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('file1', models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d')),
                ('file2', models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d')),
                ('views', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
