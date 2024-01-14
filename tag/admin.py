from django.contrib import admin
from tag.models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        obj.save()
