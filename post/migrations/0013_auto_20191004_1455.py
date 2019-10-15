# Generated by Django 2.1 on 2019-10-04 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20191004_1455'),
        ('post', '0012_auto_20191004_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_id', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detect_date', models.DateField()),
                ('product_name', models.CharField(choices=[('', '선택하세요')], max_length=100)),
                ('product_etc', models.CharField(max_length=200)),
                ('detect_name', models.CharField(choices=[('', '선택하세요')], max_length=100)),
                ('start_point', models.CharField(max_length=100)),
                ('end_point', models.CharField(max_length=100)),
                ('dport', models.CharField(max_length=200)),
                ('direction', models.CharField(choices=[('', '선택하세요')], max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('attack_type', models.CharField(choices=[('', '선택하세요'), ('웹 해킹 시도 탐지', '웹 해킹 시도 탐지'), ('악성코드 감염 의심 트래픽 탐지', '악성코드 감염 의심 트래픽 탐지'), ('서비스 거부(Dos/DDos) 공격 탐지', '서비스 거부(Dos/DDos) 공격 탐지'), ('정보 수집 시도 탐지', '정보 수집 시도 탐지'), ('기타', '기타')], max_length=100)),
                ('content', models.TextField()),
                ('countermeasures', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='responsetype',
            name='symptom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Symptom'),
        ),
    ]
