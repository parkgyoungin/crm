from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils import timezone
from choice.choices import get_choices
from django.db.models import Q

class SendEmail(AbstractBaseUser):
    email = models.EmailField(max_length=100)

    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'

class UserManager(BaseUserManager):
    def create_user(self,userid, name, nickname ,email, password=None):
        if not userid:
            raise ValueError('Users must have an userid')

        user = self.model(
            userid = userid,
            user_name = name,
            nickname = nickname,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, user_name , nickname, email, password):
        user = self.create_user(
            userid,
            user_name,
            nickname,
            email,
            password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    userid = models.CharField(
        verbose_name='아이디',
        max_length=50,
        unique=True,
    )

    user_name = models.CharField(
        verbose_name='이름',
        max_length=50,
    )

    email = models.EmailField(
        verbose_name='이메일',
        max_length=255,
    )

    #email_password = models.CharField(max_length=100, null=True, blank=True)

    nickname = models.CharField(
        verbose_name='닉네임',
        max_length=30,
        unique=True
    )
    date_joined = models.DateTimeField(
        verbose_name='가입일자',
        default=timezone.now
    )
    password = models.CharField(
        verbose_name='비밀번호',
        max_length=255
    )
    is_admin = models.BooleanField(default=False)

    send_email = models.ForeignKey(SendEmail, on_delete=models.CASCADE, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['nickname', ]

    class Meta:
        ordering = ('-date_joined',)

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin



class Address(models.Model):
    address = models.CharField(max_length=200)

    address_old = models.CharField(max_length=200, null=True, blank=True)

    detail = models.CharField(max_length=100, null=True, blank=True)

    zip_code = models.CharField(max_length=20, null=True, blank=True)

    note = models.CharField(max_length=100, null=True, blank=True)

    location = models.CharField(max_length=20, choices=get_choices('location'))

    overseas_address = models.CharField(max_length=200, null=True, blank=True)


class Security(models.Model):
    contract = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('contract'))

    block_permis = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('block_permis'))

    send_date = models.DateField(null=True, blank=True)

    interlock_date = models.DateField(null=True, blank=True)

    serial = models.CharField(max_length=100, null=True, blank=True)

    expiry_date = models.DateField(null=True, blank=True)

    firmware = models.CharField(max_length=50, null=True, blank=True)

    equipment_class = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('equipment_class'))

    ownership = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('ownership'))

    access_permis = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('access_permis'))

    termination_date = models.DateField(null=True, blank=True)

    termination_reason = models.CharField(max_length=50, null=True, blank=True)

    ips_rule = models.CharField(max_length=30, null=True, blank=True, choices=get_choices('ips_check'))

    sys_log = models.CharField(max_length=30, null=True, blank=True, choices=get_choices('ips_check'))

    icmp = models.CharField(max_length=30, null=True, blank=True, choices=get_choices('ips_check'))

    snmp = models.CharField(max_length=30, null=True, blank=True, choices=get_choices('ips_check'))

    snmp_sub = models.CharField(max_length=30, null=True, blank=True, choices=get_choices('snmp_sub'))

    etc = models.CharField(max_length=255, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

class Internal(models.Model):
    contract = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('contract'))

    apply_n = models.IntegerField(null=True, blank=True)

    interlock_date = models.DateField(null=True, blank=True)

    ip = models.CharField(max_length=100, null=True, blank=True)

    termination_date = models.DateField(null=True, blank=True)

    termination_reason = models.CharField(max_length=50, null=True, blank=True)

    etc = models.CharField(max_length=255, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

class Virus(models.Model):
    contract = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('contract'))

    apply_n = models.IntegerField(null=True, blank=True)

    interlock_date = models.DateField(null=True, blank=True)

    termination_date = models.DateField(null=True, blank=True)

    termination_reason = models.CharField(max_length=50, null=True, blank=True)

    etc = models.CharField(max_length=255, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

class Ransomware(models.Model):
    contract = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('contract'))

    apply_n = models.IntegerField(null=True, blank=True)

    interlock_date = models.DateField(null=True, blank=True)

    termination_date = models.DateField(null=True, blank=True)

    termination_reason = models.CharField(max_length=50, null=True, blank=True)

    etc = models.CharField(max_length=255, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='회사이름')

    tenant = models.BooleanField(blank=True, default=False, verbose_name='입주기업')

    ss_security = models.CharField(max_length=20, choices=get_choices('service_state'))

    ss_internal = models.CharField(max_length=20, choices=get_choices('service_state'))

    ss_virus = models.CharField(max_length=20, choices=get_choices('service_state'))

    ss_ransomware = models.CharField(max_length=20, choices=get_choices('service_state'))

    im_state = models.CharField(max_length=20, blank=True, default='0000')

    business_type = models.CharField(max_length=50, choices=get_choices('business_type'))

    business_etc = models.CharField(max_length=50, blank=True, null=True)

    business_uptae = models.CharField(max_length=50, choices=get_choices('business_uptae'))

    business_class = models.CharField(max_length=50, choices=get_choices('business_class'))

    join_path = models.CharField(max_length=50, choices=get_choices('join_path'))

    top_name = models.CharField(max_length=50)

    #top_email = models.EmailField()

    homepage = models.CharField(max_length=100, null=True, blank=True)

    business_n = models.IntegerField(verbose_name='사업자번호')

    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='company_address')

    #install_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='install_address')

    operation_etc = models.CharField(max_length=50, null=True, blank=True)

    large_etc = models.CharField(max_length=50, null=True, blank=True)

    major_etc = models.CharField(max_length=50, null=True, blank=True)

    closed_etc = models.CharField(max_length=50, null=True, blank=True)

    defense_etc = models.CharField(max_length=50, null=True, blank=True)

    smart_etc = models.CharField(max_length=50, null=True, blank=True)

    large_scale = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('large_scale'))

    major_partner = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('major_partner'))

    closed_net = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('closed_net'))

    defense_industry = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('defense_industry'))

    smart_factory = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('smart_factory'))

    manager_m_name = models.CharField(max_length=50)

    manager_m_depart = models.CharField(max_length=50)

    manager_m_phone = models.IntegerField()

    manager_m_cphone = models.IntegerField()

    manager_m_email = models.EmailField()

    manager_s_name = models.CharField(max_length=50, null=True, blank=True)

    manager_s_depart = models.CharField(max_length=50, null=True, blank=True)

    manager_s_phone = models.IntegerField(null=True, blank=True)

    manager_s_cphone = models.IntegerField(null=True, blank=True)

    manager_s_email = models.EmailField(null=True, blank=True)

    manager_f_name = models.CharField(max_length=50, null=True, blank=True)

    manager_f_depart = models.CharField(max_length=50, null=True, blank=True)

    manager_f_phone = models.IntegerField(null=True, blank=True)

    manager_f_cphone = models.IntegerField(null=True, blank=True)

    manager_f_email = models.EmailField(null=True, blank=True)

    #bill_send_date = models.IntegerField()

    etc = models.TextField(null=True, blank=True)

    file = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    security = models.ForeignKey(Security, on_delete=models.DO_NOTHING)

    internal = models.ForeignKey(Internal, on_delete=models.DO_NOTHING)

    virus = models.ForeignKey(Virus, on_delete=models.DO_NOTHING)

    ransomware = models.ForeignKey(Ransomware, on_delete=models.DO_NOTHING)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    views = models.PositiveIntegerField(default=0)

    colors = {
        '미사용': 'white',
        '사용중': 'green',
        '개통예정': 'darkviolet',
        '해지': 'red',
    }
    def get_area(self):
        try:
            address = self.address.address
            space = address.find(' ')
        except:
            address = ''
        return address[:space]

    def get_business_category(self):
        field_list = [
            self.large_scale,
            self.major_partner,
            self.closed_net,
            self.defense_industry,
            self.smart_factory,
            self.operation_etc
        ]
        datas = []
        for field in field_list:
            if field:
                datas.append(field)

        result = ', '.join(datas)
        html = '<span class="bscate">%s</span>'%result
        return html

    def get_im_state(self):
        value_list = [
            '보안관제',
            '내부보안',
            '악성코드',
            '랜섬웨어'
        ]
        result = ''
        for i, bite in enumerate(self.im_state):
            if int(bite):
                result += value_list[i] + '  '

        return result

    def get_address(self):
        ad = self.address
        result = '%s, %s  %s'%(
            ad.address,
            ad.detail,
            ad.note,
        )
        return result



    def set_ss_state_color(self):
        colors = dict(self.colors)
        colors['미사용'] = 'gainsboro'
        ids = [
            'ss_security',
            'ss_internal',
            'ss_virus',
            'ss_ransomware',
        ]
        result = []
        for id in ids:
            val = eval('self.%s'%id)
            color = colors[val]
            result.append('#%s {color:%s; font-weight:bold;}'%(id,color))
        return result

    def set_security_color(self):
        color = self.colors[self.ss_security]
        return 'style="color:%s; font-weight:bold;"'%color

    def set_internal_color(self):
        color = self.colors[self.ss_internal]
        return 'style="color:%s; font-weight:bold;"'%color

    def set_virus_color(self):
        color = self.colors[self.ss_virus]
        return 'style="color:%s; font-weight:bold;"'%color

    def set_ransomware_color(self):
        color = self.colors[self.ss_ransomware]
        return 'style="color:%s; font-weight:bold;"'%color

    @staticmethod
    def get_state():
        result = {
            'all' : {
                'ss_security' : {},
                'ss_internal' : {},
                'ss_virus' : {},
                'ss_ransomware' : {},
                'total' : {
                    'use':0,
                    'soon':0,
                    'termination':0,
                    'sum':0,
                    'sum_all':0,
                }
            },
            'defense' : {
                'ss_security': {},
                'ss_internal': {},
                'ss_virus': {},
                'ss_ransomware': {},
                'total' : {
                    'use':0,
                    'soon':0,
                    'termination':0,
                    'sum':0,
                    'sum_all':0,
                }
            },
        }
        fields = ['ss_security', 'ss_internal', 'ss_virus', 'ss_ransomware']
        Q1 = lambda field : "Q(%s = '사용중')"%field
        Q2 = lambda field : "Q(%s = '개통예정')"%field
        Q3 = lambda field : "Q(%s = '해지')"%field
        Q4 = lambda field : "Q(%s = '사용중') & Q(defense_industry__icontains = '방위')"%field
        Q5 = lambda field: "Q(%s = '개통예정') & Q(defense_industry__icontains = '방위')" % field
        Q6 = lambda field: "Q(%s = '해지') & Q(defense_industry__icontains = '방위')" % field


        for field in fields:
            use = result['all'][field]['use'] = Company.get_state_by_conditions(field, Q1)
            soon = result['all'][field]['soon'] = Company.get_state_by_conditions(field, Q2)
            termination = result['all'][field]['termination'] = Company.get_state_by_conditions(field, Q3)
            sum = result['all'][field]['sum'] = Company.get_state_by_conditions(field, Q1, Q2)
            sum_all = result['all'][field]['sum_all'] = Company.get_state_by_conditions(field, Q1, Q2, Q3)
            result['all'][field]['content'] = "사용중 : %s , 개통예정 : %s, 해지 : %s <br> %s+%s (%s+%s+%s)"%(
                result['all'][field]['use'], result['all'][field]['soon'], result['all'][field]['termination'],
                result['all'][field]['use'], result['all'][field]['soon'],
                result['all'][field]['use'], result['all'][field]['soon'], result['all'][field]['termination']
            )
            # += total
            result['all']['total']['use'] += use
            result['all']['total']['soon'] += soon
            result['all']['total']['termination'] += termination
            result['all']['total']['sum'] += sum
            result['all']['total']['sum_all'] += sum_all

            use = result['defense'][field]['use'] = Company.get_state_by_conditions(field, Q4)
            soon = result['defense'][field]['soon'] = Company.get_state_by_conditions(field, Q5)
            termination = result['defense'][field]['termination'] = Company.get_state_by_conditions(field, Q6)
            sum = result['defense'][field]['sum'] = Company.get_state_by_conditions(field, Q4, Q5)
            sum_all = result['defense'][field]['sum_all'] = Company.get_state_by_conditions(field, Q4, Q5, Q6)
            result['defense'][field]['content'] = "사용중 : %s , 개통예정 : %s, 해지 : %s <br> %s+%s (%s+%s+%s)" % (
                result['defense'][field]['use'], result['defense'][field]['soon'], result['defense'][field]['termination'],
                result['defense'][field]['use'], result['defense'][field]['soon'],
                result['defense'][field]['use'], result['defense'][field]['soon'], result['defense'][field]['termination']
            )
            # += total
            result['defense']['total']['use'] += use
            result['defense']['total']['soon'] += soon
            result['defense']['total']['termination'] += termination
            result['defense']['total']['sum'] += sum
            result['defense']['total']['sum_all'] += sum_all

        result['all']['total']['content'] = "사용중 : %s , 개통예정 : %s, 해지 : %s <br> %s+%s (%s+%s+%s)" % (
            result['all']['total']['use'], result['all']['total']['soon'], result['all']['total']['termination'],
            result['all']['total']['use'], result['all']['total']['soon'],
            result['all']['total']['use'], result['all']['total']['soon'], result['all']['total']['termination']
        )
        result['defense']['total']['content'] = "사용중 : %s , 개통예정 : %s, 해지 : %s <br> %s+%s (%s+%s+%s)" % (
            result['defense']['total']['use'], result['defense']['total']['soon'], result['defense']['total']['termination'],
            result['defense']['total']['use'], result['defense']['total']['soon'],
            result['defense']['total']['use'], result['defense']['total']['soon'], result['defense']['total']['termination']
        )

        return result

    @staticmethod
    def get_state_by_conditions(field, *args):
        all_Q = Q()

        for q in args:
            all_Q = all_Q | eval(q(field))

        return Company.objects.filter(all_Q).count()






















