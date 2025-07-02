from django.contrib import admin
from .models import Bookmark,Like,Comment,CommentLike


admin.site.register(Bookmark)
admin.site.register(Like)
# admin.site.register(Comment)
admin.site.register(CommentLike)

@admin.register(Comment) #admin 데코리이션 ~꾸미기?!~

class CommentAdmin(admin.ModelAdmin):
    list_display=("id","user","todo","content","created_at","like_count")

    def like_count(self,obj):
        return obj.likes.count()