from django import template
from django.template.defaultfilters import dictsort, dictsortreversed

register = template.Library()

@register.filter
def order_by(value, arg):
    table_row = arg.split('_')[0]
    
    if 'reversed' in arg:
        return dictsortreversed(value, table_row)
    
    return dictsort(value, table_row)