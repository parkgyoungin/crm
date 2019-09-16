# Generated by Django 2.1 on 2019-09-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetectionPat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_name', models.CharField(max_length=50)),
                ('risk', models.CharField(max_length=50)),
                ('cve', models.CharField(max_length=50)),
                ('rule_rdate', models.DateField()),
                ('rule_udate', models.DateField()),
                ('pro_state', models.CharField(max_length=50)),
                ('equ_class', models.CharField(max_length=50)),
                ('att_class', models.CharField(max_length=50)),
                ('att_type', models.CharField(max_length=50)),
                ('pat_analysis', models.TextField()),
                ('countermeasures', models.TextField()),
            ],
        ),
    ]
