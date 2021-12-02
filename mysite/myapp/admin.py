from django.contrib import admin

from .models import Category,Photo,AboutTitle

class PhotoAdmin(admin.StackedInline):
    model = Photo

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]

    class Meta:
        model = Category

class PhotoAdmin(admin.ModelAdmin):
    
    list_display = ('id', "image","image_preview")
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True

admin.site.register(Photo, PhotoAdmin)

@admin.register(AboutTitle)
class AboutTitle(admin.ModelAdmin):
    pass