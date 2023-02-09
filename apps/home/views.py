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
from .openai_conn import get_opengpt_output

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

# Custom Pages
def create_doc(request):
    if request.method == 'POST':
        try:
            type = request.POST.get('input-type')
            app = request.POST.get('input-application')
            audience = request.POST.get('input-audience')
            scenario = request.POST.get('input-scenario')
            bu_str = request.POST.get('input-bu')
            additional_info = request.POST.get('input-information')
            business_unit, created = BusinessUnit.objects.get_or_create(name = bu_str.lower())

            heading = f"{app}: {type}"
            
            content, tags = get_opengpt_output(type, app, audience, scenario, additional_info)
            #content, tags = ("Lorem Ipsum", ['Tag 1', 'Tag 2'])

            documentation, created = Documentation.objects.get_or_create(
                heading = heading,
                content = content,
            )
            documentation.business_unit.add(business_unit)
            documentation.save()
            print(f"Created Documentation: {created}")

            for tag_content in tags:
                tag, created = Tag.objects.get_or_create(
                    content = tag_content,
                )
                tag.documentations.add(documentation)
                tag.save()
            print(f"Created Tag {tag_content}: {created}")
        except Exception as e:
            print(e)
            return redirect(f'/error')
        else:
            return redirect(f'/success')
    return render(request, 'home/wizard.html', {})
    
def success(request):
    documentations = Documentation.objects.all()
    return render(request, 'home/tables-success.html', {"documentations":documentations})

def documentations(request):
    documentations = Documentation.objects.all()
    return render(request, 'home/tables.html', {"documentations":documentations})

def filtered_documentations(request,bu):
    business_unit = BusinessUnit.objects.filter(name=bu)
    documentations = Documentation.objects.filter(business_unit=business_unit)
    return render(request, 'home/tables.html', {"documentations":documentations})


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