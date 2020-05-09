from django.contrib import admin

from HomePage.models import (UserProfileInfo,
							UserProfilePostMessage, 
							Blog,BlogComment,AdminPost,Subscription,DSAd)

# Register your models here.

class UserProfileInfoModel(admin.ModelAdmin):
	readonly_fields = ['user_update_date',]

class UserPostMessage(admin.ModelAdmin):
	readonly_fields = ['user_post_date',]

class BlogCommentField(admin.ModelAdmin):
	readonly_fields = ['post','create_date',]

class UserBlog(admin.ModelAdmin):
	readonly_fields = ['blog_post_date',]

class AdminPostFields(admin.ModelAdmin):
	readonly_fields = ['blog_post_date',]

class SubscriptionFields(admin.ModelAdmin):
	readonly_fields = ['created',]




admin.site.register(UserProfileInfo,UserProfileInfoModel)
admin.site.register(Blog,UserBlog)
admin.site.register(BlogComment,BlogCommentField)
admin.site.register(UserProfilePostMessage,UserPostMessage)
admin.site.register(AdminPost,AdminPostFields)
admin.site.register(Subscription,SubscriptionFields)
admin.site.register(DSAd)

