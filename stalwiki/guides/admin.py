from django.contrib import admin

from .models import Tag, Guide


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'tag_list')
    list_filter = ('user', 'tags')
    search_fields = ('name', 'description', 'user__username')
    filter_horizontal = ('tags',)

    def tag_list(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])