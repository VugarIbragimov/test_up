from django.http import HttpResponse
from django.template import loader


def draw_menu(request, menu_title):
    template = loader.get_template('tree/menu.html')
    context = {'menu_name': menu_title}
    return HttpResponse(template.render(context, request))
