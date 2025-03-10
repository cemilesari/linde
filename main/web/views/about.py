from django.shortcuts import render,redirect
from django.views import View
from django.utils.translation import ugettext as _
from django.contrib import messages


class AboutUs(View):
    template_name = "web/pages/about.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:about_tr_view')
        return render(request, self.template_name,self.ctx)
    def post(self,request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class AboutUsTR(View):
    template_name = "web/pages/about-tr.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:about_view')
        return render(request, self.template_name,self.ctx)
    def post(self,request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)