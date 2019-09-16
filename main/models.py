from django.db import models

class BeneficCom(models.Model):
    cu_name = models.CharField(max_length=100)

    cu_tenant = models.BooleanField()

    cu_cnumber = models.CharField(max_length=100)

    cu_serstate_security = models.CharField(max_length=100)

    cu_serstate_information = models.CharField(max_length=100)

    cu_serstate_virus = models.CharField(max_length=100)

    cu_serstate_ransomware = models.CharField(max_length=100)

    cu_imastate_security = models.BooleanField()

    cu_imastate_information = models.BooleanField()

    cu_imastate_virus = models.BooleanField()

    cu_imastate_ransomware = models.BooleanField()

    #업태
    cu_business = models.CharField(max_length=100)

    # 업종
    cu_comclass = models.CharField(max_length=100)

    # 가입경로
    cu_path = models.CharField(max_length=100)

    # 대표자명
    cu_rname = models.CharField(max_length=100)

    # 대표자 이메일
    cu_remail = models.EmailField(max_length=100)

    # 홈페이지
    cu_homepage = models.CharField(max_length=100)

    # 사업자번호
    cu_bnumber = models.CharField(max_length=100)

    # 주소
    cu_address = models.CharField(max_length=100)

    # 설치주소
    cu_iaddress = models.CharField(max_length=100)

    # 대규모 입주단지
    op_imove = models.CharField(max_length=100)

    # 대기업 협력사
    op_lpartner = models.CharField(max_length=100)

    # 패쇄망
    op_closer = models.CharField(max_length=100)

    # 방위산업
    op_defense = models.CharField(max_length=100)

    # 기타
    op_etc = models.CharField(max_length=100)

    # 정:이름
    ma_name = models.CharField(max_length=100)

    # 정:부서
    ma_circles = models.CharField(max_length=100)

    # 정:휴대폰
    ma_phone = models.CharField(max_length=100)

    # 정:회사전화
    ma_cphone = models.CharField(max_length=100)

    # 정:이메일
    ma_email = models.EmailField()

    # 부:이름
    re_name = models.CharField(max_length=100)

    # 부:부서
    re_circles = models.CharField(max_length=100)

    # 부:휴대폰
    re_phone = models.CharField(max_length=100)

    # 부:회사전화
    re_cphone = models.CharField(max_length=100)

    # 부:이메일
    re_email = models.EmailField()

    # 요금:이름
    ch_name = models.CharField(max_length=100)

    # 요금:부서
    ch_circles = models.CharField(max_length=100)

    # 요금:휴대폰
    ch_phone = models.CharField(max_length=100)

    # 요금:회사전화
    ch_cphone = models.CharField(max_length=100)

    # 요금:이메일
    ch_email = models.EmailField()

    # 세금계산서발송일
    bc_sdate = models.DateField()

    # 기타사항
    bc_etc = models.TextField()

    # 첨부파일
    bc_file = models.FileField(upload_to='files/%Y/%m/%d')

class Security(models.Model):
    beneficCom = models.ForeignKey(BeneficCom, on_delete=models.CASCADE, related_name='security')
    # 계약사항
    se_contract = models.CharField(max_length=100)

    # 선차단 권한
    se_pblock = models.CharField(max_length=100)

    # 보고서 발송일
    se_sdate = models.DateField()

    # 연동일
    se_cdate = models.DateField()

    # 시리얼번호
    se_serial = models.CharField(max_length=100)

    # 라이선스 만료일
    se_edate = models.DateField()

    # 장비펌웨어
    se_firmware = models.CharField(max_length=100)

    # 장비분류
    se_eqclass = models.CharField(max_length=100)

    # 소유권
    se_ownership = models.CharField(max_length=100)

    # 접근권한
    se_access = models.CharField(max_length=100)

    # ips/check
    se_ips = models.CharField(max_length=100)

    # 해지일
    se_tdate = models.DateField()

    # 해지일 사유
    se_treason = models.CharField(max_length=100)

    # 기타사항
    se_etc = models.TextField()



class Internal(models.Model):
    beneficCom = models.ForeignKey(BeneficCom, on_delete=models.CASCADE, related_name='internal')
    # 계약사항
    in_contract = models.CharField(max_length=100)

    # 신청대수
    in_apply = models.PositiveIntegerField()

    # 연동일
    in_cdate = models.DateField()

    # ip
    in_ip = models.TextField()

    # 해지일
    in_tdate = models.DateField()

    # 해지일-사유
    in_treason = models.CharField(max_length=100)

    # 기타사항
    in_etc = models.TextField()

class Virus(models.Model):
    beneficCom = models.ForeignKey(BeneficCom, on_delete=models.CASCADE, related_name='virus')
    # 계약사항
    vi_contract = models.CharField(max_length=100)

    # 신청대수
    vi_apply = models.PositiveIntegerField()

    # 연동일
    vi_cdate = models.DateField()

    # 해지일
    vi_tdate = models.DateField()

    # 해지일-사유
    vi_treason = models.CharField(max_length=100)

    # 기타사항
    vi_etc = models.TextField()

class Ransomware(models.Model):
    beneficCom = models.ForeignKey(BeneficCom, on_delete=models.CASCADE, related_name='ransomware')
    # 계약사항
    ra_contract = models.CharField(max_length=100)

    # 신청대수
    ra_apply = models.PositiveIntegerField()

    # 연동일
    ra_cdate = models.DateField()

    # 해지일
    ra_tdate = models.DateField()

    # 해지일-사유
    ra_treason = models.CharField(max_length=100)

    # 기타사항
    ra_etc = models.TextField()















