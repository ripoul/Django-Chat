from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter(name='getImgName')
@stringfilter
def getImgName(value):
    strTAB = value.split('/')
    name = strTAB[len(strTAB)-1]
    return 'pp/'+name