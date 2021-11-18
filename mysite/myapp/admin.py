from django.contrib import admin

from .models import Category,Photo,AboutTitle

class PhotoAdmin(admin.StackedInline):
    model = Photo

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]

    class Meta:
        model = Category

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

@admin.register(AboutTitle)
class AboutTitle(admin.ModelAdmin):
    pass