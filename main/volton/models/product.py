from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from main.core.models import TimeStampedModel, Currency
from autoslug import AutoSlugField
from embed_video.fields import EmbedVideoField
from ckeditor_uploader.fields import RichTextUploadingField
from main.volton.models.blog import *
from django.utils.text import slugify

class CertificaEN(TimeStampedModel):
    class Meta:
        verbose_name = _("EN Sertifika")
        verbose_name_plural = _("EN Sertifikalar")
        ordering = ("-created",)
    
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Sertifika"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    
    def __str__(self):
        return self.name
class BrosEN(TimeStampedModel):
    class Meta: 
        verbose_name = _("EN Broşür")
        verbose_name_plural = _("EN Broşürler")
        ordering = ("-created",)
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Broşür"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    def __str__(self):
        return self.name
class KlavuzEN(TimeStampedModel):
    class Meta: 
        verbose_name = _("EN Kullanım Klavuzu")
        verbose_name_plural = _("EN Kullanım Klavuzları")
        ordering = ("-created",)
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Kullanım Klavuzu"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    def __str__(self):
        return self.name
class Products(TimeStampedModel):
    class Meta:
        verbose_name = _("EN Ürün")
        verbose_name_plural = _("EN Ürünler ")
        ordering = ("-created",)
    MCCB        = "MCCB"
    CONTACTOR   = "CONTACTOR"
    MMS         = "MMS"
    MSB         = "MSB"
    SPD         = "SPD"
    ACB         = "ACB"
    EMPR        = "EMPR"
    CATEGORY = (
        (MCCB        , _("MCCB")),
        (CONTACTOR   , _("CONTACTOR")),
        (MMS         , _("MMS")),
        (MSB         , _("MSB")),
        (SPD         , _("SPD")),
        (ACB         , _("ACB")),
        (EMPR        , _("EMPR")),
    )
    title    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.TextField(_("Ürün Yazı"), blank=True)
    image    = models.ImageField(_("Ürün Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    image2    = models.ImageField(_("Ürün Resim 2"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    image3    = models.ImageField(_("Ürün Resim 2"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    al_body  = models.TextField(_("Özellik 1"), blank=True)
    al_body2  = models.TextField(_("Özellik 2"), blank=True)
    al_body3  = models.TextField(_("Özellik 3"), blank=True)
    al_body4  = models.TextField(_("Özellik 4"), blank=True)
    al_body5  = models.TextField(_("Özellik 5"), blank=True)
    tek_body   = RichTextUploadingField(_("Teknik Özellikler"), blank=True)
    category = models.CharField(_("Select Category"),choices=CATEGORY, default=MCCB, max_length=500)
    brosur   = models.ForeignKey(BrosEN, verbose_name=_("Brosür"),blank=True,null=True,on_delete=models.CASCADE)
    kullanim   = models.ForeignKey(KlavuzEN, verbose_name=_("Kullanım Kılavuzu"),blank=True,null=True,on_delete=models.CASCADE)
    video   = EmbedVideoField(blank=True) 
    certifica = models.ManyToManyField(CertificaEN, verbose_name=_("Sertifika"),blank=True, null=True)
    slug   = models.SlugField(max_length=100)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(Keywords, verbose_name=_("Keywords"),blank=True, null=True)

    def __str__(self):
        return self.title
class Certifica(TimeStampedModel):
    verbose_name = _("Sertifika")
    verbose_name_plural = _("Sertifikalar")
    ordering = ("-created",)
    
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Sertifika"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    
    def __str__(self):
        return self.name
class Bros(TimeStampedModel):
    class Meta:
        verbose_name = _("Broşür")
        verbose_name_plural = _("Broşürler")
        ordering = ("-created",)
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Broşür"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    def __str__(self):
        return self.name
class Klavuz(TimeStampedModel):
    verbose_name = _("TR Kullanım Klavuzu")
    verbose_name_plural = _("TR Kullanım Klavuzları")
    ordering = ("-created",)
    name    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.FileField(_("Kullanım Klavuzu"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True)
    def __str__(self):
        return self.name
class ProductsTr(TimeStampedModel):
    class Meta:
        verbose_name = _("Gazlar ve Ekipmanlar")
        verbose_name_plural = _("Gazlar ve Ekipmanlar")
        ordering = ("-created",)

    title    = models.CharField(_("Başlık"), max_length=200,)
    body     = models.TextField(_("Ürün Yazı"), blank=True)
    image    = models.ImageField(_("Ürün Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    image2    = models.ImageField(_("Ürün Resim 2"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    image3    = models.ImageField(_("Ürün Resim 2"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    al_body  = models.TextField(_("Özellik 1"), blank=True)
    al_body2  = models.TextField(_("Özellik 2"), blank=True)
    al_body3  = models.TextField(_("Özellik 3"), blank=True)
    al_body4  = models.TextField(_("Özellik 4"), blank=True)
    al_body5  = models.TextField(_("Özellik 5"), blank=True)
    tek_body   = RichTextUploadingField(_("Teknik Özellikler"), blank=True)
    #category = models.CharField(_("Kategori Seçiniz"),choices=CATEGORY, default=MCCB, max_length=500)
    brosur   = models.ForeignKey(Bros, verbose_name=_("Brosür"),blank=True,null=True,on_delete=models.CASCADE)
    #kullanim   = models.ForeignKey(Klavuz, verbose_name=_("Kullanım Kılavuzu"),blank=True,null=True,on_delete=models.CASCADE)
    video   = EmbedVideoField(blank=True) 
    #certifica = models.ManyToManyField(Certifica, verbose_name=_("Sertifika"),blank=True, null=True)
    slug   = models.SlugField(unique=True, blank=True)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(KeywordsTR, verbose_name=_("Keywords"),blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while ProductsTr.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)  # Normal kaydetme işlemini gerçekleştir


class Industries(TimeStampedModel):
    class Meta:
        verbose_name = _("Endüstriler")
        verbose_name_plural = _("Endüstriler")
        ordering = ("-created",)

    title    = models.CharField(_("Başlık"), max_length=200,)
    image    = models.ImageField(_("Ürün Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    tek_body   = RichTextUploadingField(_("Özellikler"), blank=True)
    slug   = models.SlugField(unique=True, blank=True)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(KeywordsTR, verbose_name=_("Keywords"),blank=True, null=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Industries.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)  # Normal kaydetme işlemini gerçekleştir

