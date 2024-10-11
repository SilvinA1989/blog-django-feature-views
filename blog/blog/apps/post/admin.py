from django.contrib import admin
from apps.post.models import Post, PostImage, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'creation_date',
                    'modification_date', 'allow_comments')
    search_fields = ('title', 'content',
                     'author__username', 'author__id', 'id')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('creation_date', 'allow_comments')
    ordering = ('-creation_date',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'post', 'creation_date')
    search_fields = ('content', 'author__username',
                     'author__id', 'post__title', 'id')
    list_filter = ('creation_date', 'author')
    ordering = ('-creation_date',)


def activate_images(modeladmin, request, queryset):
    updated = queryset.update(active=True)
    modeladmin.message_user(request, f"{updated} imagenes fueron activadas correctamente")
activate_images.short_description = "Activar imagenes seleccionadas"

def deactivate_images(modeladmin, request, queryset):
    updated = queryset.update(active=False)
    modeladmin.message_user(request, f"{updated} imagenes fueron desactivadas correctamente")
deactivate_images.short_description = "Desactivar imagenes seleccionadas"

class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'active')
    search_fields = ('post__title', 'post__id', 'image', 'id')
    list_filter = ('active',)
    ordering = ('-creation_date',)
    actions = [activate_images, deactivate_images]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostImage, PostImageAdmin)
