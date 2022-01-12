from django import template

from app.models import Availability
register =template.Library()

@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success'
    return 'bg-danger'

@register.simple_tag
def get_availibilities(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')

@register.simple_tag
def is_division_selected(selected_division, pk):
    if selected_division == str(pk):
        return 'selected'
    return ''
    

@register.simple_tag
def is_city_selected(selected_city_id, pk):
    if selected_city_id == str(pk):
        return 'selected'
    return ''
     