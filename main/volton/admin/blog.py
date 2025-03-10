from __future__ import unicode_literals, absolute_import
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from main.volton.models import *

@admin.register(BlogTr)
class BlogAdmin_Tr(admin.ModelAdmin):
	list_display = ("title","image","created",)
	search_fields = ("title",) 
	date_hierarchy = "created"


@admin.register(ProductsTr)
class ProductAdmin_Tr(admin.ModelAdmin):
	list_display = ("title","image","created",)  
	search_fields = ("title",) 
	date_hierarchy = "created"

@admin.register(Industries)
class IndustriesAdmin(admin.ModelAdmin):
	list_display = ("title","image","created",)  
	search_fields = ("title",) 
	date_hierarchy = "created"


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
	list_display = ("full_name", "email", "body","tel","created",)
	search_fields = ("full_name",) 
	date_hierarchy = "created"


@admin.register(Iletisim)
class IletisimAdmin(admin.ModelAdmin):
	list_display = ("full_name", "email", "body","tel","created",)
	search_fields = ("full_name",) 
	date_hierarchy = "created"

 
@admin.register(Certifica)
class CertificaTRAdmin(admin.ModelAdmin):
	list_display = ("name", "body", "created",)
	search_fields = ("name",) 
	date_hierarchy = "created"
 
@admin.register(Bros)
class BrosTRAdmin(admin.ModelAdmin):
	list_display = ( "name","body", "created",)
	date_hierarchy = "created"

@admin.register(Klavuz)
class KlavuzENAdmin(admin.ModelAdmin):
	list_display = ( "name","body", "created",)
	date_hierarchy = "created"


@admin.register(Kvkk)
class KvkkAdmin(admin.ModelAdmin):
	list_display = ( "title","body", "created",)
	date_hierarchy = "created"

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
	list_display = ( "title","body", "created",)
	date_hierarchy = "created"

@admin.register(KeywordsTR)
class KwywordsTRAdmin(admin.ModelAdmin):
	list_display = ("name",  "created",)
	search_fields = ("name",) 
	date_hierarchy = "created"
 