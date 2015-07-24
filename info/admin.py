from django.contrib import admin
from django import forms
from .models import Project
from .models import Gallery
from .models import Image
from sorl.thumbnail.admin import AdminImageMixin


class ProjectAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectAdminForm, self).__init__(*args, **kwargs)
        self.fields['cover_image'].queryset = Image.objects.filter(gallery=self.instance.gallery)

class ImageInline(AdminImageMixin, admin.TabularInline):
    model = Image
    extra = 0


class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm


admin.site.register(Project, ProjectAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image)
