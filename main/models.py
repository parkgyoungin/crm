from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils import timezone

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

class TbBeneficcom(models.Model):
    bc_number = models.AutoField(primary_key=True, default=0)
    bc_date = models.DateTimeField(auto_now_add=True)
    bc_cu_name = models.CharField(max_length=50)
    bc_cu_namein = models.BooleanField(default=False)
    bc_cu_cnumber = models.IntegerField()
    bc_cu_rname = models.CharField(max_length=50)
    bc_cu_remail = models.EmailField()
    bc_cu_bnumber = models.IntegerField(unique=True)
    bc_cu_comclass = models.CharField(max_length=50)
    bc_cu_business = models.CharField(max_length=50)
    bc_cu_path = models.CharField(max_length=50)
    bc_cu_homepage = models.CharField(max_length=150, blank=True, null=True)
    bc_cu_address = models.CharField(max_length=100)
    bc_cu_iaddress = models.CharField(max_length=100)
    bc_im_security = models.BooleanField(default=False)
    bc_im_internal = models.BooleanField(default=False)
    bc_im_virus = models.BooleanField(default=False)
    bc_im_ransomware = models.BooleanField(default=False)
    bc_ss_security = models.CharField(max_length=10)
    bc_ss_internal = models.CharField(max_length=10)
    bc_ss_virus = models.CharField(max_length=10)
    bc_ss_ransomware = models.CharField(max_length=10)
    bc_op_lmove = models.CharField(max_length=10, blank=True, null=True)
    bc_op_lpartner = models.CharField(max_length=10, blank=True, null=True)
    bc_op_closure = models.CharField(max_length=10, blank=True, null=True)
    bc_op_defense = models.CharField(max_length=10, blank=True, null=True)
    bc_op_etc = models.CharField(max_length=50, blank=True, null=True)
    bc_ma_name = models.CharField(max_length=10, blank=True, null=True)
    bc_ma_circles = models.CharField(max_length=50, blank=True, null=True)
    bc_ma_phone = models.CharField(max_length=50, blank=True, null=True)
    bc_ma_cphone = models.CharField(max_length=50, blank=True, null=True)
    bc_ma_email = models.EmailField()
    bc_re_name = models.CharField(max_length=10, blank=True, null=True)
    bc_re_circles = models.CharField(max_length=50, blank=True, null=True)
    bc_re_phone = models.CharField(max_length=50, blank=True, null=True)
    bc_re_cphone = models.CharField(max_length=50, blank=True, null=True)
    bc_re_email = models.EmailField()
    bc_ch_name = models.CharField(max_length=10, blank=True, null=True)
    bc_ch_circles = models.CharField(max_length=50, blank=True, null=True)
    bc_ch_phone = models.CharField(max_length=50, blank=True, null=True)
    bc_ch_cphone = models.CharField(max_length=50, blank=True, null=True)
    bc_ch_email = models.EmailField()
    bc_sdate = models.IntegerField()
    bc_etc = models.TextField(blank=True, null=True)
    bc_file = models.FileField(blank=True, null=True)

    class Meta:
        db_table = 'tb_beneficcom'

class TbSecurity(models.Model):
    se_number = models.AutoField(primary_key=True, default=0)
    se_date = models.DateTimeField(auto_now_add=True)
    se_benumber = models.ForeignKey(TbBeneficcom, models.DO_NOTHING, db_column='se_benumber')
    se_contract = models.CharField(max_length=50)
    se_pblock = models.CharField(max_length=80)
    se_serial = models.CharField(max_length=80)
    se_sdate = models.DateField()
    se_cdate = models.DateField()
    se_edate = models.DateField()
    se_tdate = models.DateField()
    se_treason = models.CharField(max_length=80, blank=True, null=True)
    se_firmware = models.CharField(max_length=50)
    se_eqclass = models.CharField(max_length=50)
    se_ownership = models.CharField(max_length=50)
    se_access = models.CharField(max_length=50)
    se_ipsrule = models.BooleanField(default=False)
    se_syslog = models.BooleanField(default=False)
    se_icmp = models.BooleanField(default=False)
    se_snmp = models.BooleanField(default=False)
    se_etc = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_security'

class TbInternal(models.Model):
    in_number = models.AutoField(primary_key=True, default=0)
    in_date = models.DateTimeField(auto_now_add=True)
    in_benumber = models.ForeignKey(TbBeneficcom, models.DO_NOTHING, db_column='in_benumber')
    in_contract = models.CharField(max_length=50)
    in_apply = models.IntegerField()
    in_cdate = models.DateField()
    in_ip = models.CharField(max_length=50)
    in_tdate = models.DateField()
    in_treason = models.CharField(max_length=80, blank=True, null=True)
    in_etc = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_internal'

class TbVirus(models.Model):
    vi_number = models.AutoField(primary_key=True, default=0)
    vi_date = models.DateTimeField(auto_now_add=True)
    vi_benumber = models.ForeignKey(TbBeneficcom, models.DO_NOTHING, db_column='vi_benumber')
    vi_contract = models.CharField(max_length=50)
    vi_apply = models.IntegerField()
    vi_cdate = models.DateField()
    vi_tdate = models.DateField()
    vi_treason = models.CharField(max_length=80, blank=True, null=True)
    vi_etc = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_virus'

class TbRansom(models.Model):
    ra_number = models.AutoField(primary_key=True, default=0)
    ra_date = models.DateTimeField(auto_now_add=True)
    re_benumber = models.ForeignKey(TbBeneficcom, models.DO_NOTHING, db_column='re_benumber')
    ra_contract = models.CharField(max_length=50)
    ra_apply = models.IntegerField()
    ra_cdate = models.DateField()
    ra_tdate = models.DateField()
    ra_treason = models.CharField(max_length=80, blank=True, null=True)
    ra_etc = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_ransom'


















