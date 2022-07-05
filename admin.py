from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

# Register your models here.

class directionCosmetAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = directionCosmet
        fields = '__all__'


# --- Направления ---
class directionCosmetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'get_html_photo', 'is_published', 'dir_category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')
    prepopulated_fields = {"slug": ("title",)}
    #fields - список редактируемых полей
    fields = ('title', 'slug', 'description', 'content', 'photo', 'get_html_photo', 'dir_category','is_published', 'time_created', 'time_updated')
    readonly_fields = ('time_created', 'time_updated', 'get_html_photo')
    form = directionCosmetAdminForm

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=85")

    get_html_photo.short_description = "Миниатюра"

class directionImgGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_created', 'date_modified', 'get_html_photo', 'album')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'album')
    list_filter = ('date_created', 'date_modified', 'album')
    readonly_fields = ('get_html_photo', 'date_created', 'date_modified' )

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=85")

    get_html_photo.short_description = "Миниатюра"

# --- категории Направления ---
class directionCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

#--- Направления
admin.site.register(directionCosmet, directionCosmetAdmin)
admin.site.register(directionImgGallery, directionImgGalleryAdmin)
#--- категории Направления
admin.site.register(directionCategory, directionCategoryAdmin)
