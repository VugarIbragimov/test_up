from django import template
from tree.models import MenuItem


register = template.Library()


@register.inclusion_tag('tree/tag_menu.html')
def draw_menu(menu_title):
    menu_items = MenuItem.objects.filter(title=menu_title)
    return {'menu_items': menu_items}
