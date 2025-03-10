from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, render, redirect, HttpResponse
from django.urls import reverse
from django.conf import settings
from django.views.generic import View
from main.volton.models import *
from django.template import RequestContext
class MainView(View):
    template_name = 'web/index.html'
    ctx = {}

    def get(self, request, *args, **kwargs):
        #blogs = Blog.objects.all()
        #blogstr = BlogTr.objects.all()
        #products = Products.objects.all().order_by("-created")[:3]
        productstr = ProductsTr.objects.all().order_by("-created")[:3]
        slider = Slider.objects.all()
        slider_en = SliderEN.objects.all()
        bloglist = Blog.objects.all().order_by("-created")[:3]
        bloglist_tr = BlogTr.objects.all().order_by("-created")[:3]
        self.ctx = {
          'slider':slider,
          'bloglist':bloglist,
          'bloglist_tr':bloglist_tr,
          'slider_en' : slider_en,
        }
        return render(request, self.template_name, self.ctx)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)



def handler404(request, exception):
  data = {}
  return render(request,'web/pages/404.html', data)