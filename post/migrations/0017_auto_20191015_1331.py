# Generated by Django 2.1 on 2019-10-15 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0016_auto_20191015_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectionpattern',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detectionpattern',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]