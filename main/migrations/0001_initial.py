# Generated by Django 2.1 on 2019-10-16 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userid', models.CharField(max_length=50, unique=True, verbose_name='아이디')),
                ('user_name', models.CharField(max_length=50, verbose_name='이름')),
                ('email', models.EmailField(max_length=255, verbose_name='이메일')),
                ('nickname', models.CharField(max_length=30, unique=True, verbose_name='닉네임')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='가입일자')),
                ('password', models.CharField(max_length=255, verbose_name='비밀번호')),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date_joined',),
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('address_old', models.CharField(blank=True, max_length=200, null=True)),
                ('detail', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(choices=[('', 'test')], max_length=20)),
                ('overseas_address', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='회사이름')),
                ('tenant', models.BooleanField(blank=True, default=False, verbose_name='입주기업')),
                ('ss_security', models.CharField(choices=[('', 'test')], max_length=20)),
                ('ss_internal', models.CharField(choices=[('', 'test')], max_length=20)),
                ('ss_virus', models.CharField(choices=[('', 'test')], max_length=20)),
                ('ss_ransomware', models.CharField(choices=[('', 'test')], max_length=20)),
                ('im_state', models.CharField(blank=True, default='0000', max_length=20)),
                ('business_type', models.CharField(choices=[('', 'test')], max_length=50)),
                ('business_etc', models.CharField(blank=True, max_length=50, null=True)),
                ('business_uptae', models.CharField(choices=[('', 'test')], max_length=50)),
                ('business_class', models.CharField(choices=[('', 'test')], max_length=50)),
                ('join_path', models.CharField(choices=[('', 'test')], max_length=50)),
                ('top_name', models.CharField(max_length=50)),
                ('homepage', models.CharField(blank=True, max_length=100, null=True)),
                ('business_n', models.IntegerField(verbose_name='사업자번호')),
                ('operation_etc', models.CharField(blank=True, max_length=50, null=True)),
                ('large_etc', models.CharField(blank=True, max_length=50, null=True)),
                ('major_etc', models.CharField(blank=True, max_length=50, null=True)),
                ('closed_etc', models.CharField(blank=True, max_length=50, null=True)),
                ('defense_etc', models.CharField(blank=True, max_length=50, null=True)),
                ('smart_etc', models.CharField(blank=True, max_length=50, null=True)),
                ('large_scale', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('major_partner', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('closed_net', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('defense_industry', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('smart_factory', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('manager_m_name', models.CharField(max_length=50)),
                ('manager_m_depart', models.CharField(max_length=50)),
                ('manager_m_phone', models.IntegerField()),
                ('manager_m_cphone', models.IntegerField()),
                ('manager_m_email', models.EmailField(max_length=254)),
                ('manager_s_name', models.CharField(blank=True, max_length=50, null=True)),
                ('manager_s_depart', models.CharField(blank=True, max_length=50, null=True)),
                ('manager_s_phone', models.IntegerField(blank=True, null=True)),
                ('manager_s_cphone', models.IntegerField(blank=True, null=True)),
                ('manager_s_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('manager_f_name', models.CharField(blank=True, max_length=50, null=True)),
                ('manager_f_depart', models.CharField(blank=True, max_length=50, null=True)),
                ('manager_f_phone', models.IntegerField(blank=True, null=True)),
                ('manager_f_cphone', models.IntegerField(blank=True, null=True)),
                ('manager_f_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('etc', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='company_address', to='main.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Internal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('apply_n', models.IntegerField(blank=True, null=True)),
                ('interlock_date', models.DateField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=100, null=True)),
                ('termination_date', models.DateField(blank=True, null=True)),
                ('termination_reason', models.CharField(blank=True, max_length=50, null=True)),
                ('etc', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ransomware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('apply_n', models.IntegerField(blank=True, null=True)),
                ('interlock_date', models.DateField(blank=True, null=True)),
                ('termination_date', models.DateField(blank=True, null=True)),
                ('termination_reason', models.CharField(blank=True, max_length=50, null=True)),
                ('etc', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('block_permis', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('send_date', models.DateField(blank=True, null=True)),
                ('interlock_date', models.DateField(blank=True, null=True)),
                ('serial', models.CharField(blank=True, max_length=100, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('firmware', models.CharField(blank=True, max_length=50, null=True)),
                ('equipment_class', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('ownership', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('access_permis', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('termination_date', models.DateField(blank=True, null=True)),
                ('termination_reason', models.CharField(blank=True, max_length=50, null=True)),
                ('ips_rule', models.CharField(blank=True, choices=[('', 'test')], max_length=30, null=True)),
                ('sys_log', models.CharField(blank=True, choices=[('', 'test')], max_length=30, null=True)),
                ('icmp', models.CharField(blank=True, choices=[('', 'test')], max_length=30, null=True)),
                ('snmp', models.CharField(blank=True, choices=[('', 'test')], max_length=30, null=True)),
                ('snmp_sub', models.CharField(blank=True, choices=[('', 'test')], max_length=30, null=True)),
                ('etc', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.CharField(blank=True, choices=[('', 'test')], max_length=50, null=True)),
                ('apply_n', models.IntegerField(blank=True, null=True)),
                ('interlock_date', models.DateField(blank=True, null=True)),
                ('termination_date', models.DateField(blank=True, null=True)),
                ('termination_reason', models.CharField(blank=True, max_length=50, null=True)),
                ('etc', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='internal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Internal'),
        ),
        migrations.AddField(
            model_name='company',
            name='ransomware',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Ransomware'),
        ),
        migrations.AddField(
            model_name='company',
            name='security',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Security'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='virus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Virus'),
        ),
        migrations.AddField(
            model_name='user',
            name='send_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.SendEmail'),
        ),
    ]
