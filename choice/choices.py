from .models import Choice
#('value', 'visible'),
serstate = [
    ('', '선택하세요'),
    ('사용중', '사용중'),
    ('개통예정', '계통예정'),
    ('해지', '해지'),
    ('미사용', '미사용'),
]

sample = [
    ('', '선택하세요'),
    ('sample','sample'),
]

sample_etc = [
    ('', '선택하세요'),
    ('sample', 'sample'),
    ('etc', '기타'),
]

op = [
    ('', '선택하세요'),
    ('테크노파크','테크노파크'),
    ('지식재산센터', '지식재산센터'),
    ('포스코ICT', '포스코ICT'),
]

com_class = [
    ('success', '완료'),
]




service_state = [
    ('', '선택하세요'),
    ('미사용', '미사용'),
    ('사용중', '사용중'),
    ('개통예정', '계통예정'),
    ('해지', '해지'),
]

business_type = [
    ('', '선택하세요'),
    ('법인', '법인'),
    ('개인', '개인'),
    ('직접입력', '직접입력')
]

business_uptae = [
    ('','선택하세요'),
    ('전기/전자','전기/전자'),
    ('화학/섬유','화학/섬유'),
    ('기계/소재','기계/소재'),
    ('정보/통신','정보/통신'),
    ('바이오/의료','바이오/의료'),
    ('에너지자원','에너지자원'),
    ('지식서비스','지식서비스'),
    ('기타','기타'),
]

business_class = [
    ('','선택하세요'),
    ('제조업(C)','제조업(C)'),
    ('광업(B)','광업(B)'),
    ('건설업(F)','건설업(F)'),
    ('운수 및 창고업(H)','운수 및 창고업(H)'),
    ('정보통신업(J)','정보통신업(J)'),
    ('사업시설 관리, 사업 지원 및 임대 서비스업(N)','사업시설 관리, 사업 지원 및 임대 서비스업(N)'),
    ('보건업 및 사회복지 서비스업(Q)','보건업 및 사회복지 서비스업(Q)'),
    ('농업, 임업 및 어업(A)','농업, 임업 및 어업(A)'),
    ('전기, 가스, 증기 및 공기조절 공급업(D)','전기, 가스, 증기 및 공기조절 공급업(D)'),
    ('도매 및 소매업(G)','도매 및 소매업(G)'),
    ('숙박 및 음식점업(I)','숙박 및 음식점업(I)'),
    ('금융 및 보험업(K)','금융 및 보험업(K)'),
    ('전문, 과학 및 기술 서비스업(M)','전문, 과학 및 기술 서비스업(M)'),
    ('예술, 스포츠 및 여가관련 서비스업(R)','예술, 스포츠 및 여가관련 서비스업(R)'),
    ('수도, 하수 및 폐기물 처리, 원료 재생업(E)','수도, 하수 및 폐기물 처리, 원료 재생업(E)'),
    ('교육 서비스업(P)','교육 서비스업(P)'),
    ('협회 및 단체, 수리 및 기타 개인 서비스업(S)','협회 및 단체, 수리 및 기타 개인 서비스업(S)'),
    ('부동산업(L)','부동산업(L)'),
    ('공공 행정, 국방 및 사회보장 행정(O)','공공 행정, 국방 및 사회보장 행정(O)'),
]

join_path = [
    ('','선택하세요'),
    ('홈페이지 및 이메일 안내','홈페이지 및 이메일 안내'),
    ('유선연락 및 방문','유선연락 및 방문'),
    ('보안교육 및 컨설팅','보안교육 및 컨설팅'),
    ('지인 및 기관 추천','지인 및 기관 추천'),
    ('지식재산센터','지식재산센터'),
]

large_scale = [
    ('','선택하세요'),
    ('직접입력(추가)','직접입력(추가)'),
    ('(재)경기도경제과학진흥원','(재)경기도경제과학진흥원'),
    ('(재)서울산업진흥원','(재)서울산업진흥원'),
    ('한국기술벤처재단','한국기술벤처재단'),
    ('경기과학기술대학교','경기과학기술대학교'),
    ('경기콘텐츠진흥원','경기콘텐츠진흥원'),
    ('고대_산학재단','고대_산학재단'),
    ('대구디지털산업진흥원(ICT파크)','대구디지털산업진흥원(ICT파크)'),
    ('대구디지털산업진흥원(IDEA허브)','대구디지털산업진흥원(IDEA허브)'),
    ('대구디지털산업진흥원(글로벌게임센터)','대구디지털산업진흥원(글로벌게임센터)'),
    ('대구디지털산업진흥원(스마트콘텐츠상용화지원센터)','대구디지털산업진흥원(스마트콘텐츠상용화지원센터)'),
    ('대구디지털산업진흥원(청년ICT창업성장센터)','대구디지털산업진흥원(청년ICT창업성장센터)'),
    ('대구테크노파크','대구테크노파크'),
    ('동국대학교_산학협력단','동국대학교_산학협력단'),
    ('르호봇창업보육센터','르호봇창업보육센터'),
    ('삼송테크노밸리','삼송테크노밸리'),
    ('수원시창업지원센터','수원시창업지원센터'),
    ('신구대_창업보육센터','신구대_창업보육센터'),
    ('연세대원주산학협력단','연세대원주산학협력단'),
    ('용인송담대학교산학협력단','용인송담대학교산학협력단'),
    ('울산정보보호지원센터','울산정보보호지원센터'),
    ('울산정보산업진흥원','울산정보산업진흥원'),
    ('청주대학교창업보육센터','청주대학교창업보육센터'),
    ('충북보건과학대학교산학협력단','충북보건과학대학교산학협력단'),
    ('한양대학교창업보육센터','한양대학교창업보육센터'),
]

major_partner = [
    ('','선택하세요'),
    ('직접입력(추가)', '직접입력(추가)'),
    ('KT','KT'),
    ('대우조선해양','대우조선해양'),
    ('삼성전자협력사','삼성전자협력사'),
    ('삼영무역','삼영무역'),
    ('세종텔레콤','세종텔레콤'),
    ('실리콘웍스','실리콘웍스'),
    ('포스코ICT','포스코ICT'),
    ('포스코켐텍','포스코켐텍'),
    ('풍산안강사업장','풍산안강사업장'),
    ('한국항공우주산업','한국항공우주산업'),
    ('현대기아자동차그룹','현대기아자동차그룹'),
    ('현대자동차협력사','현대자동차협력사'),
]

closed_net = [
    ('', '선택하세요'),
    ('o', 'o'),
    ('x', 'x'),
]

defense_industry = [
    ('','선택하세요'),
    ('방위산업체','방위산업체'),
    ('방위산업협력기업','방위산업협력기업'),
]

smart_factory = [
    ('','선택하세요'),
    ('직접입력(추가)','직접입력(추가)'),
    ('스마트공장','스마트공장'),
]

contract = [
    ('','선택하세요'),
    ('1년 약정','1년 약정'),
    ('2년 약정','2년 약정'),
    ('3년 약정','3년 약정'),
    ('4년 약정','4년 약정'),
    ('5년 약정','5년 약정'),
]

equipment_class = [
    ('','선택하세요'),
    ('UTM','UTM'),
    ('IPS','IPS'),
    ('DDoS','DDoS'),
    ('FW','FW'),
]

ownership = [
    ('','선택하세요'),
    ('임대장비','임대장비'),
    ('씨애너스장비','씨애너스장비'),
    ('고객장비','고객장비'),
    ('KAITS자산','KAITS자산'),
]

access_permis = [
    ('','선택하세요'),
    ('admin','admin'),
    ('Read','Read'),
    ('R/W','R/W'),
    ('None','None'),
]

ips_check = [
    ('','선택하세요'),
    ('사용','사용'),
    ('미사용','미사용'),
]

snmp_sub = [
    ('','선택하세요'),
    ('v1','v1'),
    ('v2c','v2c'),
    ('v3','v3'),
]

process_state = [
    ('처리중','처리중'),
    ('처리완료', '처리완료')
]

reply = [
    ('회신', '회신'),
    ('미회신', '미회신')
]

division = [
    ('','선택하세요'),
    ('네트워크 장애 통보','네트워크 장애 통보'),
    ('방화벽 정책 설정 지원','방화벽 정책 설정 지원'),
    ('IPS 정책 설정 지원','IPS 정책 설정 지원'),
    ('보안관제 기술지원','보안관제 기술지원'),
    ('내부정보 기술지원','내부정보 기술지원'),
    ('악성코드 기술지원','악성코드 기술지원'),
    ('랜섬웨어 기술지원','랜섬웨어 기술지원'),
]

process_method = [
    ('유선통화', '유선통화'),
    ('E-mail', 'E-mail'),
    ('원격지원', '원격지원'),
    ('SMS', 'SMS'),
    ('기타', '기타')
]

se_equipment_class = [
    ('TrusGuard', 'TrusGuard'),
    ('Fortigate', 'Fortigate'),
    ('SNIPER', 'SNIPER'),
    ('secui', 'secui'),
    ('PaloAlto', 'PaloAlto'),
    ('기타', '기타'),
]

attack_class = [
    ('웹 해킹 시도 탐지','웹 해킹 시도 탐지'),
    ('악성코드 감염 의심 트래픽 탐지','악성코드 감염 의심 트래픽 탐지'),
    ('서비스 거부(Dos/DDos) 공격 탐지','서비스 거부(Dos/DDos) 공격 탐지'),
    ('정보 수집 시도 탐지','정보 수집 시도 탐지'),
    ('기타','기타'),
]

attack_class_sub1 = [
    ('SQL Injection','SQL Injection'),
    ('Command Injection','Command Injection'),
    ('WebShell','WebShell'),
    ('XSS(CrossSiteScript)','XSS(CrossSiteScript)'),
    ('Directory Listing','Directory Listing'),
    ('BufferOverFlow','BufferOverFlow'),
    ('Application','Application'),
    ('콘텐츠필터','콘텐츠필터'),
    ('Hijacking','Hijacking'),
    ('기타','기타'),
]

attack_class_sub2 = [
    ('Adware','Adware'),
    ('Confiker','Confiker'),
    ('기타','기타'),
]

attack_class_sub3 = [
    ('Dos/DDoS','Dos/DDoS'),
    ('기타','기타'),
]

attack_class_sub4 = [
    ('BruteForce Attack','BruteForce Attack'),
    ('Application','Application'),
    ('Scan','Scan'),
    ('Spoofing','Spoofing'),
    ('BufferOverFlow','BufferOverFlow'),
    ('기타','기타'),
]

risk = [
    ('High','High'),
    ('Medium','Medium'),
    ('Low','Low'),
]

choices = {
    'snmp_sub': snmp_sub,
    'ips_check':ips_check,
    'access_permis':access_permis,
    'ownership':ownership,
    'equipment_class':equipment_class,
    'contract':contract,
    'smart_factory':smart_factory,
    'defense_industry':defense_industry,
    'closed_net':closed_net,
    'major_partner':major_partner,
    'large_scale':large_scale,
    'join_path':join_path,
    'business_class':business_class,
    'business_uptae':business_uptae,
    'business_type':business_type,
    'service_state':service_state,
    'reply':reply,
    'process_state':process_state,
    'division':division,
    'process_method': process_method,
    'se_equipment_class' : se_equipment_class,
    'attack_class' : attack_class,
    'attack_class_sub1' : attack_class_sub1,
    'attack_class_sub2' : attack_class_sub2,
    'attack_class_sub3' : attack_class_sub3,
    'attack_class_sub4' : attack_class_sub4,
    'risk' : risk

}

widgets = {
    'ss_security' : 'service_state',
    'ss_internal' : 'service_state',
    'ss_virus' : 'service_state',
    'ss_ransomware' : 'service_state',
    'business_type' : 'business_type',
    'business_uptae' : 'business_uptae',
    'business_class' : 'business_class',
    'join_path' : 'join_path',
    'large_scale' : 'large_scale',
    'major_partner' : 'major_partner',
    'closed_net' : 'closed_net',
    'defense_industry' : 'defense_industry',
    'smart_factory' : 'smart_factory',
    'contract' : 'contract',
    'equipment_class' : 'equipment_class',
}

def insert_db():
    from .models import Choice
    for name, list in choices.items():
        for tuple in list:
            value = tuple[0]
            if value == '':
                continue
            if Choice.objects.filter(field_name=name ,value=value):
                continue
            Choice(**{'field_name': name, 'value':value}).save()

def get_choices(field_name, defalut = True):
    #return [('', 'test')]
    from .models import Choice
    choice = Choice.objects.filter(field_name=field_name)
    result = []
    if defalut:
        result = [('','선택하세요')]
    for c in choice:
        result.append( (c.value, c.value) )
    return result

#from choice.choices import insert_db
#insert_db()
