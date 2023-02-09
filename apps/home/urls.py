from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/new', views.create_doc, name='create-documentation'),
    path('/list', views.documentations, name='list-documentation'),
    path('/list/<str:bu>', views.filtered_documentations, name='filtered-documentation')
]