from django.db import models
from main.models import Company, User
from choice.choices import get_choices

class CompanyRecord(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='record')

    division = models.CharField(max_length=100, choices=get_choices('division'))

    process_method = models.CharField(max_length=100)

    process_method_etc = models.CharField(max_length=200, null=True, blank=True)

    occurr_date = models.DateTimeField()

    process_state = models.CharField(max_length=100, choices=get_choices('process_state'))

    title = models.TextField()

    content = models.TextField()

    manager_e_name = models.CharField(max_length=100, null=True, blank=True)

    manager_e_depart = models.CharField(max_length=100, null=True, blank=True)

    manager_e_phone = models.CharField(max_length=100, null=True, blank=True)

    manager_e_cphone = models.CharField(max_length=100, null=True, blank=True)

    manager_e_email = models.EmailField(max_length=100, null=True, blank=True)

    visible_m = models.BooleanField(null=True, blank=True, default=False, verbose_name='(정)')

    visible_s = models.BooleanField(null=True, blank=True, default=False, verbose_name='(부)')

    visible_e = models.BooleanField(null=True, blank=True, default=False, verbose_name='(기타)')

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

class DetectionPattern(models.Model):
    pattern_name = models.CharField(max_length=100, verbose_name='탐지 패턴명')

    risk = models.CharField(max_length=100, choices=get_choices('risk'))

    cve = models.CharField(max_length=100)

    rule_regist_date = models.DateField(null=True, blank=True)

    process_state = models.CharField(max_length=100, choices=get_choices('process_state'))

    equipment_class = models.CharField(max_length=100)

    equipment_etc = models.CharField(max_length=200, null=True, blank=True)

    attack_class = models.CharField(max_length=100)

    attack_class_etc = models.CharField(max_length=200, null=True, blank=True)

    attack_type = models.CharField(max_length=100)

    attack_type_etc = models.CharField(max_length=200, null=True, blank=True)

    content = models.TextField()

    countermeasures = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

class IPSTune(models.Model):

    title = models.CharField(max_length=200)

    content = models.TextField()

    file1 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    file2 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    views = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)


    def view(self):
        self.views += 1
        self.save()

class Schedule(models.Model):
    start_date = models.DateField()

    end_date = models.DateField()

    process_state = models.CharField(max_length=50, choices=get_choices('process_state'))

    title = models.CharField(max_length=200)

    content = models.TextField()

    file1 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    file2 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    views = models.PositiveIntegerField()


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    attendance_date = models.DateField()

    note = models.TextField()


#랜섬웨어
class RansomwarePost(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

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
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

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
