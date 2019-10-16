from django.db import models
from main.models import Company, User
from choice.choices import get_choices
import datetime
from django.db.models import Q
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

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

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)

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

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)

    def get_equipment_class(self):
        if self.equipment_class == '기타':
            return self.equipment_etc
        else:
            return self.equipment_class

    def get_attack_class(self):
        if self.equipment_class == '기타':
            return self.attack_class_etc
        else:
            return self.attack_class

    def get_attack_type(self):
        if self.equipment_class == '기타':
            return self.attack_type_etc
        else:
            return self.attack_type

class IPSTune(models.Model):

    title = models.CharField(max_length=200)

    content = models.TextField()

    file1 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    file2 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    views = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

class Answer(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey('content_type', 'object_id')

    title = models.CharField(max_length=200, verbose_name='제목')

    content = models.TextField(verbose_name='내용')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)


class Timetable(models.Model):
    title = models.CharField(max_length=200)

    content = models.TextField()

    file1 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    file2 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    answers = GenericRelation(Answer)

class Notice(models.Model):
    title = models.CharField(max_length=200)

    content = models.TextField()

    file1 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    file2 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    division = models.CharField(max_length=100, choices=get_choices('notice_division'))

    execute_date = models.DateField()

    answers = GenericRelation(Answer)

class Takeover(models.Model):
    title = models.CharField(max_length=200)

    content = models.TextField()

    file1 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    file2 = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    answers = GenericRelation(Answer)

class Symptom(models.Model):
    detect_date = models.DateField()

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=100, choices=get_choices('product_name'))

    product_etc = models.CharField(max_length=200, null=True, blank=True)

    detect_name = models.CharField(max_length=100)

    start_point = models.CharField(max_length=100)

    end_point = models.CharField(max_length=100)

    dport = models.CharField(max_length=200)

    direction = models.CharField(max_length=100, choices=get_choices('direction'))

    event_report_etc = models.CharField(max_length=100, null=True, blank=True)

    response_type_etc = models.CharField(max_length=100, null=True, blank=True)

    country = models.CharField(max_length=100)

    attack_type = models.CharField(max_length=100, choices=get_choices('attack_class'))

    content = models.TextField()

    countermeasures = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)

    def get_response_type(self):
        rts = list(self.response_type.all().values_list('value', flat=True))
        try:
            etc_idx = rts.index('기타')
            rts[etc_idx] = '기타(%s)'%(self.response_type_etc or ' ')

        except:
            pass

        return ', '.join(rts)

    def get_product_name(self):
        if self.product_name == '기타':
            return self.product_etc
        else:
            return self.product_name

class ResponseType(models.Model):
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE, related_name='response_type')

    widget_id = models.CharField(max_length=100)

    value = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)


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

    views = models.PositiveIntegerField(default=0)

    def get_popup_data(self):
        result = '작성자:%s <br> %s'%(self.user.user_name, self.content)
        return result

    @staticmethod
    def get_today():
        today = datetime.datetime.today()
        Q1 = Q(start_date__lte=today)
        Q2 = Q(end_date__gte=today)
        schedule = Schedule.objects.filter(Q1 & Q2).order_by('start_date')

        return schedule

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    attendance_date = models.DateField(auto_now_add=True)

    note = models.TextField(null=True, blank=True, verbose_name='메모')


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

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)

class Outflow(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    document_n = models.PositiveIntegerField()

    send_date = models.DateField(null=True, blank=True)

    url = models.CharField(max_length=200)

    process_state = models.CharField(max_length=30, choices=get_choices('process_state'))

    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)

    def get_weekness_as_text(self):
        weekness = self.weekness.all()
        text = ''
        for i in range(min(len(weekness), 3)):
            text += weekness[i].value + ', '
        if len(weekness) > 3:
            text += '등..'
        return text

    def get_weekness(self):
        weekness = self.weekness.all().values_list('value', flat=True)
        return ', '.join(weekness)

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
