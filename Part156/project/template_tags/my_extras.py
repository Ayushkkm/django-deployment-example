from django import template

register = template.Library()

# decorators
@register.filter(name='cu') 

def cu(value,arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

register.filter('cu',cu)