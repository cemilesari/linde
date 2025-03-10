# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url
from django.urls import path, re_path

from .views import *
from main.volton.views import *
from django.conf.urls import handler400
from main.web.views import *
app_name = 'web'



urlpatterns = [
	path('',                             MainView.as_view(),           name='main_view'),
	
	
	path('hakkimizda/',                  view=AboutUsTR.as_view(),     name='about_tr_view'),
    path('about-us/',                    view=AboutUs.as_view(),       name='about_view'),

	path('contact/',                    view=BecomeSupport.as_view(), name='enquires_view'),
	path('iletisim/',                   view=IletisimSup.as_view(),      name='iletisim'),


	path('blog-list/', 				    view=BlogView.as_view(),       name='blog_view'),
	path('blog-detail/<slug:slug>/' ,   view=BlogDetail.as_view(),     name="blog_detail"),
	path('blog/', 			    		view=BlogTrView.as_view(),     name='blog_view_new'),
	path('blog-detay/<slug:slug>/',     view=BlogTrDetail.as_view(),   name="blog_detail_tr"),


	path('gazlar-ve-ekipmanlar/',                         view=ProductTrView.as_view(),       name='per_view'),
	path('gazlar-ve-ekipmanlar/<slug:slug>/',          view=ProductDetailTrView.as_view(), name='per_detail_view'),

	path('endustiriler/',                         view=IndView.as_view(),       name='ind_view'),
	path('endustiriler/<slug:slug>/',          view=IndDetailView.as_view(), name='ind_detail_view'),


	path('mccb-urunler/',                        view=ProductTrMCCBView.as_view(),       name='mccb'),
	path('contactor-urunler/',                   view=ProductTrCONTACTORView.as_view(),       name='contactor'),
	path('mms-urunler/',                         view=ProductTrMMSView.as_view(),       name='mms'),
	path('mcb-urunler/',                         view=ProductTrMCBiew.as_view(),       name='mcb'),
	path('spd-urunler/',                         view=ProductTrSPDView.as_view(),       name='spd'),
	path('acb-urunler/',                         view=ProductTrACBView.as_view(),       name='acb'),
	path('empr-urunler/',                        view=ProductTrEMPRView.as_view(),       name='empr'),

	path('products/',                         	 view=ProductView.as_view(),       name='per_viewen'),
	path('product-detail/<slug:slug>/',          view=ProductDetailENView.as_view(), name='per_detail_viewen'),

	path('mccb-products/',                        view=ProductMCCBView.as_view(),       name='mccben'),
	path('contactor-products/',                   view=ProductCONTACTORView.as_view(),       name='contactoren'),
	path('mms-products/',                         view=ProductMMSView.as_view(),       name='mmsen'),
	path('mcb-products/',                         view=ProductMCBiew.as_view(),       name='mcben'),
	path('spd-products/',                         view=ProductSPDView.as_view(),       name='spden'),
	path('acb-products/',                         view=ProductACBView.as_view(),       name='acben'),
	path('empr-products/',                        view=ProductEMPRView.as_view(),       name='empren'),



	path('aydinlatma-metni/',          view=KvKKView.as_view(),   name="aydinlatma_metni"),
	path('privacy-policy/',       view=KvKKENView.as_view(),   name="aydinlatma_metni_en"),
]