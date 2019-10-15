from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def not_none(value):
    if value:
        return value
    else:
        return ''

@register.filter
def index(list, idx):
    if len(list[idx]) >0:
        return list[idx]
    else:
        return ''