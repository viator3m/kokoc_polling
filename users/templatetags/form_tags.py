from django import template


register = template.Library()


@register.filter
def form_class(field, class_name):
    return field.as_widget(attrs={'class': class_name})
