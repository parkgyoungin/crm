company = [
    ('name', '업체명'),
    ('id', '관리번호'),
    ('business_type', '사업자유형'),
    ('business_uptae', '업태'),
    ('business_class', '업종'),
    ('join_path', '가입경로'),
    ('top_name', '대표자명'),
    ('top_email', '대표자 이메일'),
    ('homepage', '홈페이지'),
    ('business_n', '사업자번호'),
    ('address__address', '주소')
]

# model._meta.fields - 모든필드
# field.verbose_name - 이름

def get_searchable_by_model(model):
    all_fields = model._meta.fields
    searchable = get_searchable_fields(all_fields)
    return searchable

def get_searchable_fields(fields):
    select_class = {'CharField'}
    new_fields = []
    for field in fields:
        if field.__class__.__name__ in select_class and not is_defalut(field.name, field.verbose_name):
            new_fields.append((field.name, field.verbose_name))
            #print(field.name,is_same(field.name, field.verbose_name)[1])

    return new_fields

def is_defalut(name, verbose_name):
    #print('start : ', name, verbose_name)
    if len(name) != len(verbose_name):
        return False
    else:
        for name_c, verbose_c in zip(name,verbose_name):
            #print(name_c, verbose_c)
            if name_c == verbose_c:
                continue
            elif name_c=='_' and verbose_c == ' ':
                continue
            else:
                return False
    return True


#from post.searchable import get_searchable_by_model
#from main.models import Company
#searchable = get_searchable_by_model(Company)
