
company = {
    'name' : {'name': '업체명'},
    'tenant' : {'name': '입주기업'},
    'id' : {'name': '관리번호'},
    'ss_security' : {'name': '보안관제'},
    'ss_internal' : {'name': '내부정보'},
    'ss_virus' : {'name': '악성코드'},
    'ss_ransomware' : {'name': '랜섬웨어'},
    'im_state' : {'name': '허수현황'},
    'business_type' : {'name': '사업자 유형'},
    #'business_etc' : {'name': '업체명'},
    'business_uptae' : {'name': '업태'},
    'business_class' : {'name': '업종'},
    'join_path' : {'name': '가입경로'},
    'top_name' : {'name': '대표자명'},
    'homepage' : {'name': '홈페이지'},
    'business_n' : {'name': '사업자번호'},
    'address' : {'name': '주소'},
    'large_scale' : {'name': '대규모 입주단지'},
    'major_partner' : {'name': '대기업 협력사'},
    'closed_net' : {'name': '패쇄망 운영'},
    'defense_industry' : {'name': '방위산업체'},
    'smart_factory' : {'name': '스마트 팩토리'},
    #'large_etc' : {'name': '업체명'},
    #'major_etc' : {'name': '업체명'},
    #'closed_etc' : {'name': '업체명'},
    #'defense_etc' : {'name': '업체명'},
    #'smart_etc' : {'name': '업체명'},
    'operation_etc' : {'name': '운영환경-기타'},
    'manager_m_name' : {'name': '(정)-이름'},
    'manager_m_depart' : {'name': '(정)-부서'},
    'manager_m_phone' : {'name': '(정)-휴대폰'},
    'manager_m_cphone' : {'name': '(정)-회사전화'},
    'manager_m_email' : {'name': '(정)-이메일'},
    'manager_s_name' : {'name': '(부)-이름'},
    'manager_s_depart' : {'name': '(부)-부서'},
    'manager_s_phone' : {'name': '(부)-휴대폰'},
    'manager_s_cphone' : {'name': '(부)-회사전화'},
    'manager_s_email' : {'name': '(부)-이메일'},
    'manager_f_name' : {'name': '(요금)-이름'},
    'manager_f_depart' : {'name': '(요금)-부서'},
    'manager_f_phone' : {'name': '(요금)-휴대폰'},
    'manager_f_cphone' : {'name': '(요금)-회사전화'},
    'manager_f_email' : {'name': '(요금)-이메일'},
    'etc' : {'name': '기타사항'},
}

security = {
    'contract' : {'name': '계약사항'},
    'block_permis' : {'name': '선차단 권한'},
    'send_date' : {'name': '보고서 발송일'},
    'interlock_date' : {'name': '연동일'},
    'serial' : {'name': '시리얼 번호'},
    'expiry_date' : {'name': '라이선스 만료일'},
    'firmware' : {'name': '장비 펌웨어'},
    'equipment_class' : {'name': '장비 분류'},
    'ownership' : {'name': '소유권'},
    'access_permis' : {'name': '접근 권한'},
    'termination_date' : {'name': '해지일'},
    'termination_reason' : {'name': '해지사유'},
    'ips_rule' : {'name': 'ips_rule'},
    'sys_log' : {'name': 'sys_log'},
    'icmp' : {'name': 'icmp'},
    'snmp' : {'name': 'snmp'},
    'snmp_sub' : {'name': 'snmp_sub'},
    'etc' : {'name': '기타'},
}

internal = {
    'contract' : {'name': '계약사항'},
    'apply_n' : {'name': '신청대수'},
    'interlock_date' : {'name': '연동일'},
    'ip' : {'name': 'IP'},
    'termination_date' : {'name': '해지일'},
    'termination_reason' : {'name': '해지사유'},
    'etc' : {'name': '기타'},
}

virus = {
    'contract' : {'name': '계약사항'},
    'apply_n' : {'name': '신청대수'},
    'interlock_date' : {'name': '연동일'},
    'termination_date' : {'name': '해지일'},
    'termination_reason' : {'name': '해지사유'},
    'etc' : {'name': '기타'},
}

ransomware = {
    'contract' : {'name': '계약사항'},
    'apply_n' : {'name': '신청대수'},
    'interlock_date' : {'name': '연동일'},
    'termination_date' : {'name': '해지일'},
    'termination_reason' : {'name': '해지사유'},
    'etc' : {'name': '기타'},
}

companyrecord = {

}

def get_row_data(dict, obj):
    for key in dict:
        exec('dict[key]["data"] = obj.%s'%key)

def config_company(dict, obj):
    dict['business_type']['data'] = (obj.business_type or '') + (obj.business_etc or '')
    dict['address']['data'] = obj.get_address()


def get_dict(obj):
    name = obj.__class__.__name__.lower()
    eval('get_row_data(%s, obj)'%name)
    try:
        eval('config_%s(%s, obj)' % (name, name))
    except:
        pass
    return eval('%s'%name)


#from main.models import Company
#company = Company.objects.get(id=1)
#from post.export_excel import get_dict
#get_dict(company)
