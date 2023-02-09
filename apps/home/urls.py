from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.create_doc, name='create-documentation'),
    path('list', views.documentations, name='list-documentation'),
    path('list/<str:bu>', views.filtered_documentations, name='filtered-documentation'),
    path('document/<str:h>', views.documentation_singular, name='view-documentation'),

    # Common URLs
    re_path(r'^.*\.*', views.pages, name='pages'),
]