#coding=utf-8

from django import template
register = template.Library()
#注册filter
@register.filter(name='counter')
def counter(value, page):
    pagesize = 10
    return (page - 1) * pagesize + value