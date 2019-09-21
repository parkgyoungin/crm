# Generated by Django 2.1 on 2019-09-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='business_class',
            field=models.CharField(choices=[('', 'test')], max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='business_type',
            field=models.CharField(choices=[('', 'test')], max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='business_uptae',
            field=models.CharField(choices=[('', 'test')], max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='closed_net',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='defense_industry',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='join_path',
            field=models.CharField(choices=[('', 'test')], max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='large_scale',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='major_partner',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='smart_factory',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='ss_internal',
            field=models.CharField(choices=[('', 'test')], max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='ss_ransomware',
            field=models.CharField(choices=[('', 'test')], max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='ss_security',
            field=models.CharField(choices=[('', 'test')], max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='ss_virus',
            field=models.CharField(choices=[('', 'test')], max_length=20),
        ),
        migrations.AlterField(
            model_name='internal',
            name='contract',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ransomware',
            name='contract',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='access_permis',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='contract',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='equipment_class',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='icmp',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='ips_rule',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='ownership',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='snmp',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='snmp_sub',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='sys_log',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='virus',
            name='contract',
            field=models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True),
        ),
    ]
