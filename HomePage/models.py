from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime 
from django.db.models.signals import post_save



def validate_image(image):
    file_size = image.file.size
    limit = 500
    limit_kb = 150
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit)

    #limit_mb = 8
    #if file_size > limit_mb * 1024 * 1024:
    #    raise ValidationError("Max size of file is %s MB" % limit_mb)

USER_GENDER = (
    ('Male','Male'),
    ('Female', 'Female'),
    ('Others','Others'),
)

BLOG_CATEGORY = (
	('Books', 'Books'),
	('Delhi Shades','Delhi Shades'),
    ('Event & Entertainment','Event & Entertainment'),
    ('Education', 'Education'),
    ('Fashion', 'Fashion'),
    ('Food','Food'),
    ('Gaming','Gaming'),
    ('Health & Fitness','Health & Fitness'),
    ('Kids','Kids'),
    ('Lifestyle','Lifestyle'),
    ('News','News'),
    ('Computer Programming','Computer Programming'),
    ('Politics','Politics'),
    ('Shopping','Shopping'),
    ('Social Welfare','Social Welfare'),
    ('Travel','Travel'),
    ('Technology','Technology'),
    ('Others','Others'),
)

BLOG_DELHI_SHADES = (
	('Architecture','Architecture'),
    ('Delhi Diary','Delhi Diary'),
	('Events', 'Events'),
    ('Education', 'Education'),
    ('Fashion', 'Fashion'),
    ('Food','Food'),
    ('Health & Fitness','Health & Fitness'),
    ('History','History'),
    ('Lifestyle','Lifestyle'),
    ('News','News'),
    ('Shopping','Shopping'),
    ('Social Welfare','Social Welfare'),
    ('Places','Places'),
    ('Travel','Travel'),
    ('Technology','Technology'),
    ('Others','Others'),
)



class UserProfileInfo(models.Model):

	user = models.OneToOneField(User, on_delete = models.CASCADE,)

	# additional Profile fields
	user_update_date = models.DateField(auto_now_add=True)
	user_gender = models.CharField(max_length=100, choices=USER_GENDER,)
	user_age = models.DateField(default=datetime.now, blank=True)
	user_profile_image = models.ImageField(upload_to='profile_image', blank=True,)
	user_rating = models.CharField(max_length=100, default='Bronze', blank=True)
	user_bio = models.TextField(blank=True)
	user_category = models.CharField(max_length=100, choices=BLOG_CATEGORY,)
	facebook_link = models.URLField(blank=True, unique=False)
	twitter_link = models.URLField(blank=True, unique=False)
	instagram_link = models.URLField(blank=True, unique=False)
	youtube_link = models.URLField(blank=True, unique=False)
	website_link = models.URLField(blank=True, unique=False)

	def __str__(self):
		return self.user.username

#----------------------------users subscription model--------------------------------#

class Subscription(models.Model):
	created = models.DateTimeField(auto_now_add=True, editable=False)
	creator = models.ForeignKey(User, on_delete = models.CASCADE,related_name="friendship_creator_set") # who send friend request
	subscribe = models.ForeignKey(User, on_delete = models.CASCADE, related_name="friend_set") # who accept the friend request

	def __str__(self):
		self.data =  self.creator.username+ " |subscribe| " +self.subscribe.username
		return self.data

# Create your user Post models here.
class UserProfilePostMessage(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	user_post_message = models.TextField()
	user_post_image = models.ImageField(upload_to='user_posts/user_post_images', blank=True, validators=[validate_image], help_text='The images files size must be greater than 200kb and less than 500kb. The dimensions of the photograph should be 800 (width) x 800 (height)')
	user_post_location = models.CharField(max_length=250, default='New Delhi')
	user_post_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.user.username

#--------------------------------Add Events-----------------------------------#

 #----------------------------Events SUGGESTIONS--------------------------------#

class AdminPost(models.Model):
	super_user_name = models.ForeignKey(User, on_delete = models.CASCADE)
	blog_category = models.CharField(max_length=350, choices=BLOG_DELHI_SHADES, blank=True)
	blog_heading = models.TextField()
	blog_paragraph_1 = models.TextField()
	blog_paragraph_2 = models.TextField(blank=True)
	blog_photo_1 = models.ImageField(upload_to='AdminPost', blank=True,)
	blog_photo_2 = models.ImageField(upload_to='AdminPost', blank=True,)
	blog_photo_3 = models.ImageField(upload_to='AdminPost', blank=True,)
	blog_photo_4 = models.ImageField(upload_to='AdminPost', blank=True,)
	blog_post_date = models.DateField(auto_now_add=True)
	blog_published_status = models.BooleanField(default=False)

	def __str__(self):
		self.data =  self.blog_category+ " | " +self.blog_heading
		return self.data


class Blog(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	blog_heading = models.TextField()
	blog_paragraph_1 = models.TextField()
	blog_paragraph_2 = models.TextField(blank=True)
	blog_category = models.CharField(max_length=250, choices=BLOG_CATEGORY, blank=True)
	blog_photo_1 = models.ImageField(upload_to='User Blog', blank=True,)
	blog_photo_2 = models.ImageField(upload_to='User Blog', blank=True,)
	blog_photo_3 = models.ImageField(upload_to='User Blog', blank=True,)
	blog_photo_4 = models.ImageField(upload_to='User Blog', blank=True,)
	blog_post_date = models.DateField(auto_now_add=True)
	blog_published_date = models. DateTimeField(blank=True,null=True)
	blog_published_status = models.BooleanField(default=False)

	def publish(self):
		self.blog_published_date = timezone.now()
		self.save()

	# def approve_comments(self):
	# 	return self.comments.filter(approve_comment=True)

	def __str__(self):
		self.data =  self.user.username+ " | " +self.blog_category
		return self.data

class BlogComment(models.Model):
	
	post = models.ForeignKey(Blog,on_delete = models.CASCADE)
	author = models.CharField(max_length=250)
	text = models.TextField()
	create_date = models.DateField(auto_now_add=True)
	# approve_comment = models.BooleanField(default=False)

	# def approve(self):
	# 	self.approve_comment=True
	# 	self.save()

	def __str__(self):
		return self.post.user

DELHI_SHADES_ADVERTISEMENTS = (
	('Right-Side-Ad','Right-Side-Ad'),
    ('Center-Banner','Center-Banner'),
)
class DSAd(models.Model):
	ad_name = models.CharField(max_length=500)
	ad_image = models.ImageField(upload_to='AdminPost/ads', blank=True)
	ad_category = models.CharField(max_length=250, choices=DELHI_SHADES_ADVERTISEMENTS, blank=True)
	ad_link = models.URLField(blank=True, unique=False)
	ad_published_date = models. DateTimeField(blank=True,null=True)
	ad_published_status = models.BooleanField(default=False)
	

	def __str__(self):
		return self.ad_name

