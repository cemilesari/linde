from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from main.core.models import TimeStampedModel, Currency
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Keywords(TimeStampedModel):
    class Meta:
        verbose_name = _("EN KeyWords")
        verbose_name_plural = _("EN Keywords")
        ordering = ("-created",)
        
    name    = models.CharField(_("Keyword"), max_length=200,)
    def __str__(self):
        return self.name

class Blog(TimeStampedModel):
    class Meta:
        verbose_name = _("EN Blog")
        verbose_name_plural = _("EN Blogs")
        ordering = ("-created",)
    title  = models.CharField(_("Title"), max_length=200,blank=True,null=True)
    body   = RichTextUploadingField(_("Blog Body"), blank=True)
    image  = models.ImageField(_("Blog Image"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    banner  = models.CharField(_("Banner Body"), max_length=300,)
    bannerimage  = models.ImageField(_("Banner Image"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    bannertitle  = models.CharField(_("Banner Title"), max_length=200,)
    slug = models.SlugField(max_length=100)
    titlesite = models.CharField(_("Site Title"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Description"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(Keywords, verbose_name=_("Keywords"),blank=True, null=True)

    def __str__(self):
        return self.title

    def get_dict(self):
        return dict(
            pk    = self.pk,
            title = self.title,
            body  = self.body,
            image = self.image,
            slug  = self.slug,

        )

class KeywordsTR(TimeStampedModel):
    class Meta:
        verbose_name = _("Keywords")
        verbose_name_plural = _("Keywords")
        ordering = ("-created",)
        
    name    = models.CharField(_("Keyword"), max_length=200,)
    def __str__(self):
        return self.name

class BlogTr(TimeStampedModel):
    class Meta:
        verbose_name = _("Haberler")
        verbose_name_plural = _("Haberler")
        ordering = ("-created",)
    banner  = models.CharField(_("Banner Body"), max_length=300,)
    bannerimage  = models.ImageField(_("Banner Image"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    bannertitle  = models.CharField(_("Banner Title"), max_length=200,)
    title  = models.CharField(_("Başlık"), max_length=200,blank=True,null=True)
    body   = RichTextUploadingField(_("Blog Body"), blank=True)
    image  = models.ImageField(_("Blog Resim"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    slug   = models.SlugField(max_length=100)
    titlesite = models.CharField(_("Site Başlık"), max_length=200,blank=True, null=True)
    description = models.CharField(_("Meta Açıklama"), max_length=200,blank=True, null=True)
    keywords =  models.ManyToManyField(KeywordsTR, verbose_name=_("Keywords"),blank=True, null=True)
    def __str__(self):
        return self.title

    def get_dict(self):
        return dict(
            pk    = self.pk,
            title = self.title,
            body  = self.body,
            image = self.image,
            slug  = self.slug,
        )

class Kvkk(TimeStampedModel):
    class Meta:
        verbose_name = _("Aydınlatma Metni ")
        verbose_name_plural = _("Aydınlatma Metni")
        ordering = ("-created",)
    title  = models.CharField(_("Başlık"), max_length=200,)
    body   = RichTextUploadingField(_("Blog Body"), blank=True)
    banner  = models.CharField(_("Banner Body"), max_length=300,)
    bannerimage  = models.ImageField(_("Banner Image"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    bannertitle  = models.CharField(_("Banner Title"), max_length=200,)
    def __str__(self):
        return self.title

class Slider(TimeStampedModel):
    class Meta:
        verbose_name = _(" Slider ")
        verbose_name_plural = _("Sliderlar")
        ordering = ("-created",)
    title  = models.CharField(_("Başlık"), max_length=200,)
    body   = models.TextField(_("Slider Body"), blank=True)
    button = models.CharField(_("Slider Button Url"), max_length=300,)
    sliderimage  = models.ImageField(_("Slider Image"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    def __str__(self):
        return self.title

class KvkkEN(TimeStampedModel):
    class Meta:
        verbose_name = _("EN Aydınlatma Metni ")
        verbose_name_plural = _("EN Aydınlatma Metni")
        ordering = ("-created",)
    title  = models.CharField(_("Başlık"), max_length=200,)
    body   = RichTextUploadingField(_("Blog Body"), blank=True)
    banner  = models.CharField(_("Banner Body"), max_length=300,)
    bannerimage  = models.ImageField(_("Banner Image"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    bannertitle  = models.CharField(_("Banner Title"), max_length=200,)
    def __str__(self):
        return self.title

class SliderEN(TimeStampedModel):
    class Meta:
        verbose_name = _(" EN Slider ")
        verbose_name_plural = _("EN Sliderlar")
        ordering = ("-created",)
    title  = models.CharField(_("Başlık"), max_length=200,)
    body   = models.TextField(_("Slider Body"), blank=True)
    button = models.CharField(_("Slider Button Url"), max_length=300,)
    sliderimage  = models.ImageField(_("Slider Image"), upload_to=settings.DEFAULT_BLOG_FOLDER, blank=True, default=settings.DEFAULT_BLOG_IMAGE)
    def __str__(self):
        return self.title
