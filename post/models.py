from django.db import models

class DetectionPat(models.Model):
    #IPS 탐지 패턴명
    pat_name = models.CharField(max_length=50)

    #위험도
    risk = models.CharField(max_length=50)

    #CVE
    cve = models.CharField(max_length=50)

    #IPS룰 등록일
    rule_rdate = models.DateField()

    #IPS룰 갱신일
    rule_udate = models.DateField()

    #업무처리 상태
    pro_state = models.CharField(max_length=50)

    #장비분류
    equ_class = models.CharField(max_length=50)

    etc_equ_class = models.CharField(max_length=50, null=True)

    #공격분류
    att_class = models.CharField(max_length=50)

    etc_att_class = models.CharField(max_length=50, null=True)

    #공격유형
    att_type = models.CharField(max_length=50)

    etc_att_type = models.CharField(max_length=50, null=True)

    #패턴분석
    pat_analysis = models.TextField()

    countermeasures = models.TextField()

class Comment(models.Model):
    model = models.CharField(max_length=50)

    comment = models.TextField()