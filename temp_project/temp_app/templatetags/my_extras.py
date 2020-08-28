from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out all values of 'arg' from string
    """
    return value.replace(arg,'')

# instead of this decorator is used
# register.filter('cut',cut)
