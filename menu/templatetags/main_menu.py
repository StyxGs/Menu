from django import template

from menu.models import CategoriesMenu

register = template.Library()


@register.inclusion_tag('tags/menu.html')
def draw_menu(name: str) -> dict:
    category = CategoriesMenu.objects.filter(menu__name=name)
    if not category:
        raise ValueError('Введите корректное название меню')
    else:
        return {'categories': category}
