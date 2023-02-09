# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import *

TEMPLATE = 'home/index.html'

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

# Custom Pages
def create_doc(request):
     if request.method == 'POST':
        try:
            # OBJECT CREATION
            pass
        except Exception as e:
            return redirect(f'/error')
        else:
            return redirect(f'/success')

def documentations(request):
    documentations = Documentation.objects.get.all()
    return render(request, TEMPLATE, {"documentations":documentations})

def filtered_documentations(request,bu):
    business_unit = BusinessUnit.objects.filter(name=bu)
    documentations = Documentation.objects.filter(business_unit=business_unit)
    return render(request, TEMPLATE, {"documentations":documentations})


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))