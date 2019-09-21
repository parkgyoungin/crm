from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils import timezone
from choice.choices import get_choices

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

    objects = UserManager()

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['nickname', ]

    class Meta:
        ordering = ('-date_joined',)

    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Security(models.Model):
    contract = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('contract'))

    block_permis = models.CharField(max_length=50, null=True, blank=True)

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

    ips_rule = models.CharField(max_length=30, null=True, blank=True, choices=get_choices('ips_rule'))

    sys_log = models.CharField(max_length=30, null=True, blank=True, choices=get_choices('sys_log)'))

    icmp = models.CharField(max_length=30, null=True, blank=True, choices=get_choices('ips_check'))

    snmp = models.CharField(max_length=30, null=True, blank=True, choices=get_choices('ips_check'))

    snmp_sub = models.CharField(max_length=30, null=True, blank=True, choices=get_choices('snmp_sub'))

    etc = models.CharField(max_length=255, null=True, blank=True)


class Internal(models.Model):
    contract = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('contract'))

    apply_n = models.IntegerField(null=True, blank=True)

    interlock_date = models.DateField(null=True, blank=True)

    ip = models.CharField(max_length=100, null=True, blank=True)

    termination_date = models.DateField(null=True, blank=True)

    termination_reason = models.CharField(max_length=50, null=True, blank=True)

    etc = models.CharField(max_length=255, null=True, blank=True)


class Virus(models.Model):
    contract = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('contract'))

    apply_n = models.IntegerField(null=True, blank=True)

    interlock_date = models.DateField(null=True, blank=True)

    termination_date = models.DateField(null=True, blank=True)

    termination_reason = models.CharField(max_length=50, null=True, blank=True)

    etc = models.CharField(max_length=255, null=True, blank=True)


class Ransomware(models.Model):
    contract = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('contract'))

    apply_n = models.IntegerField(null=True, blank=True)

    interlock_date = models.DateField(null=True, blank=True)

    termination_date = models.DateField(null=True, blank=True)

    termination_reason = models.CharField(max_length=50, null=True, blank=True)

    etc = models.CharField(max_length=255, null=True, blank=True)



class Company(models.Model):
    name = models.CharField(max_length=50)

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

    top_email = models.EmailField()

    homepage = models.CharField(max_length=100, null=True, blank=True)

    business_n = models.IntegerField(verbose_name='사업자번호')

    address = models.CharField(max_length=100)

    install_address = models.CharField(max_length=100)

    large_scale = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('large_scale'))

    major_partner = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('major_partner'))

    closed_net = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('closed_net'))

    defense_industry = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('defense_industry'))

    smart_factory = models.CharField(max_length=50, null=True, blank=True, choices=get_choices('smart_factory'))

    operation_etc = models.CharField(max_length=50, null=True, blank=True)

    large_etc = models.CharField(max_length=50, null=True, blank=True)

    major_etc = models.CharField(max_length=50, null=True, blank=True)

    closed_etc = models.CharField(max_length=50, null=True, blank=True)

    defense_etc = models.CharField(max_length=50, null=True, blank=True)

    smart_etc = models.CharField(max_length=50, null=True, blank=True)

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

    bill_send_date = models.IntegerField()

    etc = models.TextField(null=True, blank=True)

    file = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)

    security = models.ForeignKey(Security, on_delete=models.DO_NOTHING)

    internal = models.ForeignKey(Internal, on_delete=models.DO_NOTHING)

    virus = models.ForeignKey(Virus, on_delete=models.DO_NOTHING)

    ransomware = models.ForeignKey(Ransomware, on_delete=models.DO_NOTHING)














