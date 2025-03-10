from django.shortcuts import render,redirect
from django.views import View
from django.utils.translation import ugettext as _

from main.volton.forms import SupportForm, SupportTRForm
from main.volton.models import Support, Iletisim
from django.contrib import messages


class BecomeSupport(View):
    template_name = "web/pages/contact.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:iletisim')
        return render(request, self.template_name,self.ctx)
    def post(self,request, *args, **kwargs):
        form = SupportForm()
        full_name = request.POST.get("full_name",None)
        email         = request.POST.get("email", None)
        body           = request.POST.get("body", None)
        tel           = request.POST.get("tel", None)

        form.is_valid()
        obj = Support.objects.create(
            full_name = full_name or "Untitled Partner Name",
            email = email,
            body = body,
            tel = tel,
        )
        obj.save()
        messages.success(request, _("Great Job, Your Support application successfully."))
        self.ctx = {
            'full_name' : full_name,
            'email'         : email,
            'body'           : body,
            'tel'       : tel,
        }
        return render(request, self.template_name, self.ctx)

class IletisimSup(View):
    template_name = "web/pages/iletisim.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:enquires_view')
        return render(request, self.template_name,self.ctx)
    def post(self,request, *args, **kwargs):
        form = SupportTRForm()
        full_name = request.POST.get("full_name",None)
        email         = request.POST.get("email", None)
        body           = request.POST.get("body", None)
        tel           = request.POST.get("tel", None)
        print("email", email, "bodu", body, tel)
        form.is_valid()
        obj = Iletisim.objects.create(
            full_name = full_name or "Untitled Partner Name",
            email = email,
            body = body,
            tel = tel,
        )
        obj.save()
        messages.success(request, _("Great Job, Your Support application successfully."))
        self.ctx = {
            'full_name' : full_name,
            'email'         : email,
            'body'           : body,
            'tel'       : tel,
        }
        return render(request, self.template_name, self.ctx)