from django import template
from django.template.loader import get_template

register = template.Library()

def age_change(value, arg):
    if arg == 'change':
        value = 9999
        return value
    else:
        return value
    
    
def table():
    courses = [
        {
            'id':1,
            'name':'rahat',
            'course':'c',
            
        },
        
        {
            'id':2,
            'name':'fahat',
            'course':'c++',
            
        },
        
        {
            'id':3,
            'name':'bahat',
            'course':'c#',
            
        },
        
    ]
    return {'courses':courses}
        
       
register.filter('changeAge', age_change)

course_template = get_template('table.html')

register.inclusion_tag(course_template)(table)