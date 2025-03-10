from django.shortcuts import render,redirect
from django.views import View
from main.volton.models import *
from django.shortcuts import get_object_or_404
from main.core.utils import get_query, paginate
class ProductView(View):
    template_name= "web/pages/product.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        protrlisten = Products.objects.all()
        protrlisten = paginate(objects=protrlisten, per_page=12, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:per_view')

        self.ctx = {
            'protrlisten':protrlisten,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductDetailENView(View):
    template_name= "web/pages/product-en-detail.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        ster_tr_id = request.resolver_match.kwargs.get('slug')
        pro = get_object_or_404(Products, slug=ster_tr_id)
        self.ctx = {
            'pro' : pro,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductMCCBView(View):
    template_name= "web/pages/mccben.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        mccb = Products.objects.filter(category=Products.MCCB)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:mccb')

        self.ctx = {
            'mccb':mccb,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductCONTACTORView(View):
    template_name= "web/pages/contactoren.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        contactor = Products.objects.filter(category=Products.CONTACTOR)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:contactor')

        self.ctx = {
            'contactor':contactor,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductMMSView(View):
    template_name= "web/pages/mmsen.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        mms = Products.objects.filter(category=Products.MMS)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:mms')

        self.ctx = {
            'mms':mms,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductMCBiew(View):
    template_name= "web/pages/mcben.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        mcb = Products.objects.filter(category=Products.MSB)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:mcb')

        self.ctx = {
            'mcb':mcb,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductSPDView(View):
    template_name= "web/pages/spden.html"
    spd = {}
    def get(self, request, *args, **kwargs):
        spd = Products.objects.filter(category=Products.SPD)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:spd')

        self.ctx = {
            'spd':spd,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductACBView(View):


    template_name= "web/pages/acben.html"
    spd = {}
    def get(self, request, *args, **kwargs):
        acb = Products.objects.filter(category=Products.ACB)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:acb')

        self.ctx = {
            'acb':acb,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)


class ProductEMPRView(View):
    template_name= "web/pages/empren.html"
    spd = {}
    def get(self, request, *args, **kwargs):
        empr = Products.objects.filter(category=Products.EMPR)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'tr' :
            return redirect('web:empr')

        self.ctx = {
            'empr':empr,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductTrView(View):
    template_name= "web/pages/product-tr.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        protrlist = ProductsTr.objects.all()
        protrlist = paginate(objects=protrlist, per_page=12, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:per_viewen')

        self.ctx = {
            'protrlist':protrlist,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class ProductDetailTrView(View):
    template_name= "web/pages/product-tr-detail.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        ster_tr_id = request.resolver_match.kwargs.get('slug')
        pro = get_object_or_404(ProductsTr, slug=ster_tr_id)
        self.ctx = {
            'pro' : pro,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProductTrMCCBView(View):
    template_name= "web/pages/mccb.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        mccb = ProductsTr.objects.filter(category=ProductsTr.MCCB)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:mccben')

        self.ctx = {
            'mccb':mccb,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)




class ProductTrCONTACTORView(View):

    template_name= "web/pages/contactor.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        contactor = ProductsTr.objects.filter(category=ProductsTr.CONTACTOR)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:contactoren')

        self.ctx = {
            'contactor':contactor,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProductTrMMSView(View):
    template_name= "web/pages/mms.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        mms = ProductsTr.objects.filter(category=ProductsTr.MMS)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:mmsen')

        self.ctx = {
            'mms':mms,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProductTrMCBiew(View):

    template_name= "web/pages/mcb.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        mcb = ProductsTr.objects.filter(category=ProductsTr.MSB)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:mcben')

        self.ctx = {
            'mcb':mcb,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProductTrSPDView(View):
    template_name= "web/pages/spd.html"
    spd = {}
    def get(self, request, *args, **kwargs):
        spd = ProductsTr.objects.filter(category=ProductsTr.SPD)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:spden')

        self.ctx = {
            'spd':spd,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)

class ProductTrACBView(View):


    template_name= "web/pages/acb.html"
    spd = {}
    def get(self, request, *args, **kwargs):
        acb = ProductsTr.objects.filter(category=ProductsTr.ACB)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:acben')

        self.ctx = {
            'acb':acb,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)


class ProductTrEMPRView(View):
    template_name= "web/pages/empr.html"
    spd = {}
    def get(self, request, *args, **kwargs):
        empr = ProductsTr.objects.filter(category=ProductsTr.EMPR)
        #protrlist = paginate(objects=protrlist, per_page=6, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:empren')

        self.ctx = {
            'empr':empr,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)




class IndView(View):
    template_name= "web/pages/ind.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        protrlist = Industries.objects.all()
        protrlist = paginate(objects=protrlist, per_page=12, page=request.GET.get("page"))
        if request.LANGUAGE_CODE == 'en' :
            return redirect('web:per_viewen')

        self.ctx = {
            'protrlist':protrlist,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
class IndDetailView(View):
    template_name= "web/pages/ind-tr-detail.html"
    ctx = {}
    def get(self, request, *args, **kwargs):
        ster_tr_id = request.resolver_match.kwargs.get('slug')
        pro = get_object_or_404(Industries, slug=ster_tr_id)
        self.ctx = {
            'pro' : pro,
        }
        return render(request, self.template_name, self.ctx)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)
