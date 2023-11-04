from django.urls import path
from tree.views import draw_menu

app_name = 'tree'

urlpatterns = [
    path('<str:menu_title>/', draw_menu, name='draw_menu'),
]
