from django.shortcuts import render

def home(request):
    #get_data, DB완성시 수정요망
    count = {
        'security' : 2451,
        'information' : 2011,
        'virus' : 1521,
        'ransomware' : 412,
    }
    use_count = {
        'security': 2451,
        'information': 1512,
        'virus': 2121,
        'ransomware': 531,
    }
    content = {
        'count': count,
        'use_count': use_count,
    }

    return render(request, 'main/home.html', content)
