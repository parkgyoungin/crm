from django.db import models
from main.models import Company
from choice.choices import get_choices

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

    #장비분류-기타
    etc_equ_class = models.CharField(max_length=50, null=True)

    #공격분류
    att_class = models.CharField(max_length=50)

    #공격분류-기타
    etc_att_class = models.CharField(max_length=50, null=True)

    #공격유형
    att_type = models.CharField(max_length=50)

    #공격유형-기타
    etc_att_type = models.CharField(max_length=50, null=True)

    #패턴분석
    pat_analysis = models.TextField()

    #대응방안
    countermeasures = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

#랜섬웨어

class RansomwarePost(models.Model):
    company = models.CharField(max_length=100)

    document_n = models.PositiveIntegerField()

    send_date = models.DateField(null=True, blank=True)

    agent_name = models.CharField(max_length=100)

    agent_ip = models.CharField(max_length=50)

    detect_date = models.DateField()

    path = models.CharField(max_length=100)

    reply = models.CharField(max_length=30, choices=get_choices('reply'))

    file_name = models.CharField(max_length=100)

    process_state = models.CharField(max_length=30, choices=get_choices('process_state'))

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

class Outflow(models.Model):
    company = models.CharField(max_length=100)

    document_n = models.PositiveIntegerField()

    send_date = models.DateField(null=True, blank=True)

    url = models.CharField(max_length=200)

    process_state = models.CharField(max_length=30, choices=get_choices('process_state'))

    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    def get_weekness_as_text(self):
        weekness = self.weekness.all()
        text = ''
        for i in range(min(len(weekness), 3)):
            text += weekness[i].value + ', '
        if len(weekness) > 3:
            text += '등..'
        return text

class Weekness(models.Model):
    outflow = models.ForeignKey(Outflow, on_delete=models.CASCADE ,related_name= 'weekness')

    widget_id = models.CharField(max_length=100)

    value = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    model_name = models.CharField(max_length=50)

    model_pk = models.PositiveIntegerField()

    com_class = models.CharField(max_length=50, null=True, blank=True)

    comment = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)
