from django import forms
from django.contrib.auth.models import User
from HomePage.models import (UserProfileInfo,UserProfilePostMessage, 
                             Blog, BlogComment,AdminPost,Subscription, 
                             )
from django.contrib.auth.forms import UserChangeForm




class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():

		model= User
		fields = ['username','email','password','first_name','last_name']

class UserProfileInfoForm(forms.ModelForm):

	class Meta():
		model = UserProfileInfo
		fields = [  'user_gender',
					'user_age',
					'user_rating', 
					'user_bio' ,
					'user_category',
					'user_profile_image',
                    'facebook_link',
                    'twitter_link',
                    'instagram_link',
                    'youtube_link',
                    'website_link',
					]


class SubscriptionForm(forms.ModelForm):
    class Meta():
        model = Subscription
        fields = [
                    'creator',
                    'subscribe', 
                    ]


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

class EditUserInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = (
            'user_gender',
            'user_age',
            'user_profile_image',
            'user_bio',
            'user_category',
            'facebook_link',
            'twitter_link',
            'instagram_link',
            'youtube_link',
            'website_link',
        )
        labels = {
            'user_gender': 'Gender',
            'user_age': 'Date of birth',
            'user_profile_image': 'Profile image',
            'user_bio': 'Bio',
            'user_category': 'Blog category',
            'facebook_link': 'Facebook',
            'twitter_link': 'Twitter',
            'instagram_link':'Instagram',
            'youtube_link': 'YouTube',
            'website_link': 'Website',
        }
        help_text = { 'user_profile_image':'The images files size must be greater than 200kb and less than 500kb. The dimensions of the photograph should be 800 (width) x 800 (height)',

                    }
        widgets = {
            'user_gender': forms.Select(attrs={'class': 'form-control'},choices=USER_GENDER,),
            'user_age': forms.DateInput(attrs={'class': 'form-control'}),
            'user_profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'user_bio': forms.Textarea(attrs={'class': 'editable medium-editor-textarea form-control'}),
            'user_category': forms.Select(attrs={'class': 'form-control'},choices=BLOG_CATEGORY),
            'facebook_link': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.URLInput(attrs={'class': 'form-control'}),
            'youtube_link': forms.URLInput(attrs={'class': 'form-control'}),
            'website_link': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_link': forms.URLInput(attrs={'class': 'form-control'}),

        }



class BlogForm(forms.ModelForm):

    class Meta():
        model = Blog
        fields = [  'blog_heading',
                    'blog_category',
                    'blog_paragraph_1',
                    'blog_paragraph_2',
                    'blog_photo_1',
                    'blog_photo_2',
                    'blog_photo_3',
                    'blog_photo_4',
                    ]
        labels = {
            'blog_heading': 'Heading',
            'blog_category': 'Blog Category',
            'blog_paragraph_1': 'Introduction Paragraph',
            'blog_paragraph_2': 'Body Paragraph',
            'blog_photo_1': 'Heading Image',
            'blog_photo_2': 'Introduction Paragraph Image',
            'blog_photo_3': 'Body Paragraph Image',
            'blog_photo_4':'Body Paragraph Image',
        }
        help_text = { 'blog_photo_1':'The images files size must be greater than 200kb and less than 500kb. The dimensions of the photograph should be 800 (width) x 800 (height)',

                    }
        widgets = {
            'blog_heading': forms.TextInput(attrs={'class': 'form-control'}),
            'blog_category': forms.Select(attrs={'class': 'form-control'},choices=BLOG_CATEGORY,),
            'blog_paragraph_1': forms.Textarea(attrs={'class': 'editable medium-editor-textarea form-control'}),
            'blog_paragraph_2': forms.Textarea(attrs={'class': 'editable medium-editor-textarea form-control'}),
            'blog_photo_1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'blog_photo_2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'blog_photo_3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'blog_photo_4': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }

class BlogCommentForm(forms.ModelForm):

    class Meta():
        model = BlogComment
        fields = [  
                    'author',
                    'text',
                    ]

class AdminPostForm(forms.ModelForm):

    class Meta():
        model = AdminPost
        fields = [  'blog_category',
                    'blog_heading',
                    'blog_paragraph_1',
                    'blog_paragraph_2',
                    'blog_photo_1',
                    'blog_photo_2',
                    'blog_photo_3',
                    'blog_photo_4',
                    
                    ]
