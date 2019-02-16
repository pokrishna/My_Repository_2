from django.contrib import admin
from testapp.models import Post
from testapp.models import Comments
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']

class CommentsAdmin(admin.ModelAdmin):
    list_display=['name','email','post','body','created','updated','active']


admin.site.register(Post,PostAdmin)
admin.site.register(Comments,CommentsAdmin)
