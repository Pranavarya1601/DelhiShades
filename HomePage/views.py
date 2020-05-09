from django.shortcuts import render,redirect,get_object_or_404
from HomePage.models import (UserProfileInfo,UserProfilePostMessage,Blog,
							BlogComment,AdminPost,Subscription,DSAd,)
from HomePage.forms import (UserForm, UserProfileInfoForm,EditUserInfoForm,
							BlogForm,BlogCommentForm,AdminPostForm,
							SubscriptionForm)
from django.urls import reverse
from random import shuffle
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


#****************************Home Page ***************************************#
def home(request):
	##################################################################################################
	######################### Get Filtered data from Models ##########################################
	################################ from AdminPost Model #####################################
	heading_page_event = AdminPost.objects.all().filter(blog_category='Event & Entertainment',blog_published_status=True).order_by('-id')[0:1]
	heading_page_travel = AdminPost.objects.all().filter(blog_category='Travel',blog_published_status=True).order_by('-id')[0:1]
	heading_page_fashion = AdminPost.objects.all().filter(blog_category='Fashion',blog_published_status=True).order_by('-id')[0:1]
	heading_page_food = AdminPost.objects.all().filter(blog_category='Food',blog_published_status=True).order_by('-id')[0:1]
	heading_page_health = AdminPost.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).order_by('-id')[0:1]
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	################################ from Blog Model ##########################################
	delhi_shades = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).order_by('-id')[0:2]
	fashion1 = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).order_by('-id')[0:2]
	fashion2 = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).order_by('-id')[2:4]
	food = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).order_by('-id')[0:4]
	travel = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).order_by('-id')[0:4]
	healthfitness = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).order_by('-id')[0:4]
	shopping = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).order_by('-id')[0:4]
	technology = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).order_by('-id')[0:1]
	news = Blog.objects.all().filter(blog_category='News',blog_published_status=True).order_by('-id')[0:2]
	book = Blog.objects.all().filter(blog_category='Books',blog_published_status=True).order_by('-id')[0:2]
	education = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).order_by('-id')[0:4]
	others = Blog.objects.all().filter(blog_category='Others',blog_published_status=True).order_by('-id')[0:1]
	politics = Blog.objects.all().filter(blog_category='Politics',blog_published_status=True).order_by('-id')[0:1]
	social = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).order_by('-id')[0:2]
	gaming = Blog.objects.all().filter(blog_category='Gaming',blog_published_status=True).order_by('-id')[0:1]
	lifestyle = Blog.objects.all().filter(blog_category='Lifestyle',blog_published_status=True).order_by('-id')[0:2]
	delhi = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()

	######################### For footer add in every page ##########################################
	recent_data = Blog.objects.all().order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	user_id = User.objects.all().order_by('-id')
	################################################# Admin Advertisements ####################################################
	right_advertisement = DSAd.objects.all().filter(ad_category='Right-Side-Ad',ad_published_status=True).order_by('-id')[0:1]
	center_banner = DSAd.objects.all().filter(ad_category='Center-Banner',ad_published_status=True).order_by('-id')[0:2]
	##################################################################################################
	args={
		  'heading_page_event':heading_page_event,
		  'heading_page_travel':heading_page_travel,
		  'heading_page_fashion':heading_page_fashion,
		  'heading_page_food':heading_page_food,
		  'heading_page_health':heading_page_health,
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'fashion1':fashion1,
		  'fashion2':fashion2,
		  'food':food,
		  'travel':travel,
		  'healthfitness':healthfitness,
		  'shopping':shopping,
		  'technology':technology,
		  'news':news,
		  'book':book,
		  'education':education,
		  'others':others,
		  'politics':politics,
		  'social':social,
		  'gaming':gaming,
		  'lifestyle':lifestyle,
		  'delhi':delhi,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'user_id':user_id,
		  'center_banner':center_banner,
		  }
	return render(request,'HomePage/index.html',args)

#****************************Logout Page ***************************************#
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))


#****************************Login Page ***************************************#
def user_login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('home'))
	else:
		if request.method =='POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(username=username, password=password)

			if user:
				if user.is_active:
					login(request,user)
					print("user is active")
					return HttpResponseRedirect(reverse('home'))
				else:
					return HttpResponse("User is not registered!")
			else:
				print("Login fails")
				print("Username {} and password is {}".format(username, password))
				return HttpResponse("Invalid username and password")
		else:
			return render(request,'HomePage/UserAuthenticate/login.html')
	

#****************************user registration***************************************#

def create_account(request):
	registered = False
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('home'))
	else:
		if request.method == "POST":
			user_form =UserForm(request.POST)
			profile_form = UserProfileInfoForm(request.POST,request.FILES)

			if user_form.is_valid() and profile_form.is_valid():
				user =user_form.save()
				user.set_password(user.password)
				user.save()

				profile = profile_form.save(commit=False)
				profile.user = user

				if 'user_pic' in request.FILES:
					profile.user_pic = request.FILES['user_pic']
				profile.save()
				registered = True
			else:
				print(user_form.errors, profile_form.errors)
		else:
			user_form = UserForm()
			profile_form = UserProfileInfoForm()

		return render(request,'HomePage/UserAuthenticate/create-account.html', 
			{'user_form': user_form, 'profile_form':profile_form, 'registered': registered})



#****************************For User Account Home Page ***************************************#
@login_required
def user_profile(request):
	if request.method =='GET':
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################
		##################################################################################################
		######################### For Side panel add in every page #######################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
		right_advertisement = DSAd.objects.all().filter(ad_category='Right-Side-Ad',ad_published_status=True).order_by('-id')[0:1]

		################################ from Blog Model ##########################################
		user_blog = Blog.objects.filter(user=request.user).order_by('-blog_post_date')
		args={
		  'user_blog':user_blog,
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'right_advertisement':right_advertisement,
		  }
		return render(request, 'HomePage/User/user_profile.html', args)
	else:
		postform = UserProfilePostMessageForm(request.POST,request.FILES)
		form = postform.save(commit=False) # user ForeignKey is blank here raise error
		form.user = request.user # add ForeignKey user name
		form.save() # now Add to database
		return render(request, 'HomePage/User/user_profile.html', {})

#****************************For User Add Blog Page ***************************************#
@login_required
def addblog(request):
	form = Blog.objects.all()
	if request.method =='GET':
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################

		######################### For Side panel add in every page #######################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
		args={
		  'blog': BlogForm(),
		  'form':form,
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  }
		return render(request,'HomePage/UserBlog/blog.html', args)
	else:
		blog = BlogForm(request.POST,request.FILES)
		form = blog.save(commit=False) # user ForeignKey is blank here raise error
		form.user = request.user # add ForeignKey user name
		form.save() # now Add to database
		return redirect('user_profile')
		#return render(request, 'HomePage/User/user_profile.html', {})

#****************************For User View Blog Page***************************************#

def view_user_blog(request, blog_pk):

		if request.method == 'POST':
			author = request.POST['author']
			text = request.POST['text']
			post = blog_pk
			query = BlogComment(author=author,text=text)
			query.post_id = post
			query.save()
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
		##################################################################################################
		right_advertisement = DSAd.objects.all().filter(ad_category='Right-Side-Ad',ad_published_status=True).order_by('-id')[0:1]
		center_banner = DSAd.objects.all().filter(ad_category='Center-Banner',ad_published_status=True).order_by('-id')[0:2]

		next_blog = Blog.objects.all().filter(pk=blog_pk+1).order_by('-blog_post_date')
		previous_blog = Blog.objects.all().filter(pk=blog_pk-1).order_by('blog_post_date')
		comment = BlogComment.objects.all().filter(post=blog_pk).order_by('-create_date')
		# foreign Key matching issue user=blog_pk
		blog = get_object_or_404(Blog, pk=blog_pk,) # Add user=request.user for restrict view
		# user_blog = Blog.objects.all().order_by('-blog_post_date')
		args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'comment':comment,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'blog':blog,
		  'next_blog':next_blog,
		  'previous_blog':previous_blog,
		  'right_advertisement':right_advertisement,

			}
		return render(request,"HomePage/UserBlog/user_blog_post_view.html",args)

#****************************For User List View Blog Page***************************************#
@login_required
def list_view_blog(request):
	##################################################################################################
	################################ from AdminPost Model #####################################
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	################################ from Blog Model ##########################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	user_blog = Blog.objects.all().filter(user=request.user,blog_published_status=True).order_by('-blog_post_date')
	paginator = Paginator(user_blog, 5) # Show 25 blog per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'user_blog':user_blog,
		  'page_obj':page_obj,
			}
	
	return render(request,"HomePage/UserBlog/blog_list.html",args)

#****************************For User Update View Blog Page***************************************#
@login_required
def update_view_blog(request,blog_pk):
	blog = get_object_or_404(Blog, pk=blog_pk, user=request.user)
	if request.method == 'GET':
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
		##################################################################################################
		form = BlogForm(instance=blog)
		args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'blog':blog,
		  'form':form,
			}
		
		return render(request,"HomePage/UserBlog/update_blog.html",args)
		
	else:
		try:
			form = BlogForm(request.POST,request.FILES, instance=blog,)
			form.save()
			return redirect('list_blog')
		except ValueError:
			return render(request,"HomePage/UserBlog/update_blog.html",{'blog':blog,'form':form,'Error':'Error message: Invalid Value'})


#****************************For User Delete Blog Page***************************************#
@login_required
def delete_view_blog(request,blog_pk):
	blog = get_object_or_404(Blog, pk=blog_pk, user=request.user)

	if request.method == 'GET':
		form = BlogForm(instance=blog)
		return render(request,"HomePage/UserBlog/delete_blog.html",{'blog':blog,'form':form,})
		
	else:
		blog.delete()
		return redirect('list_blog')

#****************************For  View user profile by other users Page***************************************#

def author_profile_view(request, blog_pk):
	blog = get_object_or_404(Blog, pk=blog_pk)
	user_blog = Blog.objects.filter(user=request.user).order_by('-blog_post_date')
	
	return render(request,"HomePage/User/author_profile.html",{'blog':blog,'user_blog':user_blog,})


#****************************For Testing ***************************************#
def test(request):
	##################################################################################################
	################################ from AdminPost Model #####################################
	heading_page_event = AdminPost.objects.all().filter(blog_category='Event & Entertainment',blog_published_status=True).order_by('-id')[0:1]
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	################################ from Blog Model ##########################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	################################################# Admin Advertisements ####################################################
	right_advertisement = DSAd.objects.all().filter(ad_category='Right-Side-Ad',ad_published_status=True).order_by('-id')[0:1]
	center_banner = DSAd.objects.all().filter(ad_category='Center-Banner',ad_published_status=True).order_by('-id')[0:1]
	blog = Blog.objects.all()
	paginator = Paginator(blog, 5) # Show 25 blog per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	args={
		  'right_advertisement':right_advertisement,
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'blog':blog,
		  'page_obj':page_obj,
		  
		  'heading_page_event':heading_page_event,
			}
	return render(request,'HomePage/test.html',args)


#****************************For all Delhi Shades Posts ***************************************#
def delhi_shades(request):
	##################################################################################################
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	user_blog = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).order_by('-blog_post_date')
	paginator = Paginator(user_blog, 5) # Show 25 blog per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	##################################################################################################
	args={
		  'user_blog':user_blog,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'page_obj':page_obj,
			}
	return render(request,'HomePage/UserBlog/delhi_shades_list.html',args)

#****************************Fashion Blog ***************************************#
def fashion_blog(request):
	##################################################################################################
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	fashion = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).order_by('-blog_post_date')
	paginator = Paginator(fashion, 5) # Show 25 blog per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	##################################################################################################

	args={
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'fashion':fashion,
		  'page_obj':page_obj,
			}
	return render(request,'HomePage/UserBlog/blog_fashion_list.html',args)

#****************************For Adding User Food in Food Blog ***************************************#
def food_blog(request):
	##################################################################################################
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	food = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).order_by('-blog_post_date')
	paginator = Paginator(food, 5) # Show 25 blog per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	##################################################################################################

	args={
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'food':food,
		  'page_obj':page_obj,
			}
	return render(request,'HomePage/UserBlog/blog_food_list.html',args)

#****************************For Adding User Health in Health Blog ***************************************#
def health_blog(request):
	##################################################################################################
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()

	##################################################################################################
	health = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).order_by('-blog_post_date')
	paginator = Paginator(health, 5) # Show 25 blog per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	##################################################################################################

	args={
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'health':health,
		  'page_obj':page_obj,
			}
	return render(request,'HomePage/UserBlog/blog_health_list.html',args)

#****************************For Adding User Travel in Travel Blog ***************************************#
def travel_blog(request):
	##################################################################################################
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	travel = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).order_by('-blog_post_date')
	paginator = Paginator(travel, 5) # Show 25 blog per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	##################################################################################################

	args={
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'travel':travel,
		  'page_obj':page_obj,
			}
	return render(request,'HomePage/UserBlog/blog_travel_list.html',args)

#****************************For Adding User social in social Blog ***************************************#
def social_blog(request):
	##################################################################################################
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	social = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).order_by('-blog_post_date')
	paginator = Paginator(social, 5) # Show 25 blog per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	##################################################################################################

	args={
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'social':social,
		  'page_obj':page_obj,
			}
	return render(request,'HomePage/UserBlog/blog_social_list.html',args)



#****************************For Blog Page ***************************************#
def shopping_blog(request):
	##################################################################################################
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	shopping = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).order_by('-blog_post_date')
	paginator = Paginator(shopping, 5) # Show 25 blog per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	##################################################################################################

	args={
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'shopping':shopping,
		  'page_obj':page_obj,
			}
	return render(request,'HomePage/UserBlog/blog_shopping_list.html',args)


#****************************For Blog Page ***************************************#
def event_blog(request):
	##################################################################################################
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	event = Blog.objects.all().filter(blog_category='Event & Entertainment',blog_published_status=True).order_by('-blog_post_date')
	paginator = Paginator(event, 5) # Show 25 blog per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	##################################################################################################

	args={
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'event':event,
		  'page_obj':page_obj,
			}
	return render(request,'HomePage/UserBlog/blog_event_list.html',args)

##################################################################################################
##################################### For Admin Post #############################################
##################################################################################################

################################### For Admin Post List #######################################
def admin_post_list(request):
	##################################################################################################
	################################ from AdminPost Model #####################################
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	################################ from Blog Model ##########################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	posts = AdminPost.objects.all().filter(blog_published_status=True).order_by('-id')
	args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'comment':comment,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'blog':blog,
		  'next_blog':next_blog,
		  'previous_blog':previous_blog,
		  'posts':posts,
			}
	return render(request,'HomePage/AdminPosts/admin_post_list.html',args)


################################### For Admin Post Detail #######################################
def admin_post_detail(request, blog_pk):
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################
		##################################################################################################
		######################### For Side panel add in every page #######################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
		##################################################################################################
		next_blog = AdminPost.objects.all().filter(pk=blog_pk+1).order_by('-blog_post_date')
		previous_blog = AdminPost.objects.all().filter(pk=blog_pk-1).order_by('blog_post_date')
		# foreign Key matching issue user=blog_pk
		blog = get_object_or_404(AdminPost, pk=blog_pk,) # Add user=request.user for restrict view
		# user_blog = Blog.objects.all().order_by('-blog_post_date')
		args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'blog':blog,
		  'next_blog':next_blog,
		  'previous_blog':previous_blog,
			}
		return render(request,"HomePage/AdminPosts/admin_post_detail.html",args)

###################################Delhi diary list ############################################
def delhi_diary(request):
	##################################################################################################
	################################ from AdminPost Model #####################################
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	delhi_diary_post = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-blog_post_date')
	##################################################################################################
	args={
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_places':delhi_places,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_diary_post':delhi_diary_post,
			}
	return render(request,'HomePage/AdminPosts/delhi_diary_list.html',args)

###################################Delhi Events list ############################################
def delhi_events(request):
	##################################################################################################
	################################ from AdminPost Model #####################################
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	######################### For Side panel add in every page #######################################
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-blog_post_date')
	##################################################################################################
	args={
		  
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_places':delhi_places,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'event':event,
			}
	return render(request,'HomePage/AdminPosts/delhi_event_list.html',args)

###################################Delhi Architecture list ############################################
def delhi_architecture(request):
	##################################################################################################
	################################ from AdminPost Model #####################################
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	delhi_archi = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('blog_post_date')
	##################################################################################################
	args={
		  
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_places':delhi_places,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_archi':delhi_archi,
			}
	return render(request,'HomePage/AdminPosts/delhi_architecture_list.html',args)


###################################Delhi diary list ############################################
def delhi_history(request):
	##################################################################################################
	################################ from AdminPost Model #####################################
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	######################### For Side panel add in every page #######################################
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-blog_post_date')
	##################################################################################################
	args={
		  
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_places':delhi_places,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'history':history,
			}
	return render(request,'HomePage/AdminPosts/delhi_history_list.html',args)


###################################Delhi diary list ############################################
def delhi_places(request):
	##################################################################################################
	######################### Get Filtered data from Models ###################################
	################################ from AdminPost Model #####################################
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	######################### For Side panel add in every page #######################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-blog_post_date')
	##################################################################################################
	args={
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_places':delhi_places,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'places':places,
			}
	return render(request,'HomePage/AdminPosts/delhi_places_list.html',args)

################################### For Admin Post Display #######################################

################################### For Admin Post Display #######################################




################################### For Admin Post Display #######################################



################################### For Admin Post Display #######################################
#****************************contact Page ***************************************#
def contact(request):
	args={}
	return render(request,'HomePage/page-contact.html',args)

#****************************fashion Page ***************************************#

################################### For Author Profile List #######################################
@login_required
def author_profile_list(request):
	##################################################################################################
	################################ from AdminPost Model #####################################
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	################################ from Blog Model ##########################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	posts = User.objects.all().order_by('-id')
	args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'posts':posts,
			}
	return render(request,"HomePage/User/author_profile_list.html",args)


################################### For Admin Post Detail #######################################
def author_profile_detail(request, author_pk):
		if request.method == 'GET':
			##################################################################################################
			################################ from AdminPost Model #####################################
			delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
			delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
			delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
			delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
			delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
			################################ from Blog Model ##########################################
			##################################################################################################
			######################### For Side panel add in every page #######################################
			recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
			popular_posts = Blog.objects.all().order_by('-id')[0:4]
			delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
			fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
			food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
			travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
			healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
			shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
			technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
			education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
			social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
			# for advertisement
			right_advertisement = DSAd.objects.all().filter(ad_category='Right-Side-Ad',ad_published_status=True).order_by('-id')[0:1]
			##################################################################################################
			# foreign Key matching issue user=blog_pk
			author_details = get_object_or_404(User, pk=author_pk,)
			################################### For limited list view (paginator) ############################################################### 
			user_blog = Blog.objects.all().filter(blog_published_status=True).order_by('-blog_post_date')
			paginator = Paginator(user_blog, 5) # Show 5 blog per page.
			page_number = request.GET.get('page')
			page_obj = paginator.get_page(page_number)
			######################################## For Post counts ##########################################################
			post_counts = Blog.objects.all().filter(user = author_pk ,blog_published_status=True).count()
			follower_counter = Subscription.objects.filter(subscribe=author_pk).count()
			followering_counter = Subscription.objects.filter(creator=author_pk).count()
			##################################### For Author Subscriber list #############################################################
			subscribed= Subscription.objects.filter(creator=author_pk).values('subscribe_id').order_by('-id')
			# queryset to get all the current user subscibers list
			is_subscribed= Subscription.objects.filter(creator=request.user).values('subscribe_id').order_by('-id')
			
			##################################### For unfollow authors #############################################################
			
			# queryset to check is current author is in subscription list or not if yes,get is subscription ID
			subscribed_reg_id= Subscription.objects.filter(creator=request.user, subscribe_id=author_pk).values('id','subscribe_id').order_by('-id')
			# check if subscribed_reg_id queryset is null if null assign a temporarily value for handling null issue
			if not subscribed_reg_id:
				print('not in queryset!')
				subscription_id=0 # subscription model id assign a temporarily value for handling null issue 
			else:
				for item in subscribed_reg_id: # get the subscription queryset key and values
					if subscribed_reg_id:
						subscription_id=item['id']  # This will return subscription model id for the author subscription(followers)
						author_subscribe_id =item['subscribe_id']  # This will return author subscription id(followers)
						print('subscription model id '+str(subscription_id)+ ' subscription author id is: ' +str(author_subscribe_id))
						############# uncomment for testing purpose only ##############
						#print("is author ID is: "+str(subscribed_reg_id))
						###############################################################

			##################################################################################################
			data = author_pk # get current user ID from url(PK)
			# condition to check is subscribe_id is already in user subscription list (already friend of not)
			subscribed_id = [s['subscribe_id'] for s in is_subscribed if 'subscribe_id' in s]

			############# uncomment for testing purpose only ##############
			#print("is author ID is: "+str(data)+ " in author subscriber ID ?:"  +str(subscribed_id))
			##########################################################################################
			if data in subscribed_id:
				print('Author  already subscribed')
			else:
				print("New Author: Subscribe Now!")
			##################################################################################################
			args={
			  'delhi_shades_event':delhi_shades_event,
			  'delhi_shades':delhi_shades,
			  'delhi_diary':delhi_diary,
			  'delhi_history':delhi_history,
			  'delhi_architecture':delhi_architecture,
			  'delhi_places':delhi_places,
			  'recent_data':recent_data,
			  'popular_posts':popular_posts,
			  'delhi_shades_count':delhi_shades_count,
			  'fashion_count':fashion_count,
			  'food_count':food_count,
			  'travel_count':travel_count,
			  'healthfitness_count':healthfitness_count,
			  'shopping_count':shopping_count,
			  'technology_count':technology_count,
			  'education_count':education_count,
			  'social_count':social_count,
			  'author_details':author_details,
			  'user_blog':user_blog,
			  'post_counts':post_counts,
			  'follower_counter':follower_counter,
			  'followering_counter':followering_counter,
			  'subscribed':subscribed,
			  'subscribed_id':subscribed_id,
			  'subscribe_author':SubscriptionForm(),
			  'page_obj':page_obj,
			  'data':data,
			  'subscription_id':subscription_id,
			  'right_advertisement':right_advertisement,
				}
			return render(request,"HomePage/User/author_profile_detail.html",args)
		else:
			if request.method == "POST":
				subscribe_author = SubscriptionForm(request.POST)
				if subscribe_author.is_valid():
					form = subscribe_author.save(commit=False)
					form.creator = request.user
					form.save()
					
				else:
					print(subscribe_author.errors)
					
			else:
				subscribe_author = SubscriptionForm()
			return redirect('home')

#****************************For User Unsubscribe Author ***************************************#
@login_required
def author_unfollow(request,author_pk):
	unsubscribe_author = get_object_or_404(Subscription, pk=author_pk)
	subscription_list = Subscription.objects.filter(creator=author_pk).order_by('-id')
	if request.method == 'GET':
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################
		##################################################################################################
		######################### For Side panel add in every page #######################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
		# for advertisement
		right_advertisement = DSAd.objects.all().filter(ad_category='Right-Side-Ad',ad_published_status=True).order_by('-id')[0:1]
		form = SubscriptionForm(instance=unsubscribe_author)
		##################################################################################################
		args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'unsubscribe_author':unsubscribe_author,
		  'right_advertisement':right_advertisement,
		  'form':form,
		  'subscription_list':subscription_list
			}
		
		return render(request,"HomePage/User/Subscription/author_unfollow.html",args)
		
	else:
		unsubscribe_author.delete()
		return redirect('home')

################################### For Author unpublished blogs #####################e##################
def author_unpublished_list(request):
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################
		##################################################################################################
		######################### For Side panel add in every page #######################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
		##################################################################################################
		user_blog = Blog.objects.all().filter(blog_published_status=False, user=request.user).order_by('-blog_post_date')
		paginator = Paginator(user_blog, 5) # Show 25 blog per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		# user_blog = Blog.objects.all().order_by('-blog_post_date')
		args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'user_blog':user_blog,
		  'page_obj':page_obj,
			}
		return render(request,"HomePage/User/author_unpublished_list.html",args)


################################### For disclaimer_and_policy #######################################
def disclaimer_and_policy(request):
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################
		##################################################################################################
		######################### For Side panel add in every page #######################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
		##################################################################################################
		args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
			}
		return render(request,"HomePage/disclaimer_and_policy.html",args)

################################### For UserProfileInfo Model List #######################################
@login_required
def user_profile_info_list(request):
	##################################################################################################
	################################ from AdminPost Model #####################################
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	################################ from Blog Model ##########################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	##################################################################################################
	author_info = UserProfileInfo.objects.filter( user=request.user).order_by('-id')
	post_counts = Blog.objects.all().filter(user = request.user ,blog_published_status=True).count()
	args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'author_info':author_info,
		  'post_counts':post_counts,
			}
	return render(request,"HomePage/User/UserProfileInfo_Model/user_profile_info_list.html",args)

################################### For UserProfileInfo Model Detail #######################################
def user_profile_info_detail(request, author_pk):
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################
		##################################################################################################
		######################### For Side panel add in every page #######################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
		##################################################################################################
		# foreign Key matching issue user=blog_pk
		author_details = get_object_or_404(UserProfileInfo, pk=author_pk,user=request.user) # Add user=request.user for restrict view
		# user_blog = Blog.objects.all().order_by('-blog_post_date')
		args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'author_details':author_details,
			}
		return render(request,"HomePage/User/UserProfileInfo_Model/user_profile_info_detail.html",args)



################################### For UserProfileInfo Model Update #######################################
@login_required
def user_profile_info_update(request,author_pk):
	blog = get_object_or_404(UserProfileInfo, pk=author_pk, user=request.user)
	if request.method == 'GET':
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################
		##################################################################################################
		######################### For Side panel add in every page #######################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True)
		args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'form':EditUserInfoForm(instance=blog),
		  'blog':blog,
			}
		return render(request,"HomePage/User/UserProfileInfo_Model/user_profile_info_update.html",args)
		
	else:
		try:
			form = EditUserInfoForm(request.POST,request.FILES, instance=blog,)
			form.save()
			return redirect('user_profile')
		except ValueError:
			return render(request,"HomePage/User/UserProfileInfo_Model/user_profile_info_update.html",{'blog':blog,'form':form,'Error':'Error message: Invalid Value'})

####################################### Author Following List ###########################################################
@login_required
def user_subscription_list(request, author_pk):
	##################################################################################################
	################################ from AdminPost Model #####################################
	delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
	delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
	delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
	delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
	delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
	################################ from Blog Model ##########################################
	recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
	popular_posts = Blog.objects.all().order_by('-id')[0:4]
	delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
	fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
	food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
	travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
	healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
	shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
	technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
	education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
	social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
	# for advertisement
	right_advertisement = DSAd.objects.all().filter(ad_category='Right-Side-Ad',ad_published_status=True).order_by('-id')[0:1]
	##################################################################################################
	# foreign Key matching issue user=blog_pk
	author_details = get_object_or_404(User, pk=author_pk,) # Add user=request.user for restrict view
	subscription_list = Subscription.objects.filter(creator=author_pk).order_by('-id')
	############################## For next and previous page option ##################################
	paginator = Paginator(subscription_list, 5) # Show 5 blog per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	
	args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'author_details':author_details,
		  'subscription_list':subscription_list,
		  'page_obj':page_obj,
		  'right_advertisement':right_advertisement,
			}
	return render(request,"HomePage/User/Subscription/user_subscription_list.html",args)

####################################### Author Followers List ###########################################################
@login_required
def user_subscriber_list(request, author_pk):
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################
		##################################################################################################
		######################### For Side panel add in every page #######################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
		# for advertisement
		right_advertisement = DSAd.objects.all().filter(ad_category='Right-Side-Ad',ad_published_status=True).order_by('-id')[0:1]
		##################################################################################################
		# foreign Key matching issue user=blog_pk
		author_details = get_object_or_404(User, pk=author_pk,) # Add user=request.user for restrict view
		subscriber_list = Subscription.objects.all().filter(subscribe=author_pk).order_by('-id')
		post_counts = Blog.objects.all().filter(user = author_pk ,blog_published_status=True).count()
		follower_counter = Subscription.objects.filter(subscribe=author_pk).count()
		followering_counter = Subscription.objects.filter(creator=author_pk).count()
		############################## For next and previous page option ##################################
		paginator = Paginator(subscriber_list, 5) # Show 5 blog per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		# user_blog = Blog.objects.all().order_by('-blog_post_date')
		args={
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  'author_details':author_details,
		  'subscriber_list':subscriber_list,
		  'page_obj':page_obj,
		  'right_advertisement':right_advertisement,
			}
		return render(request,"HomePage/User/Subscription/author_subscriber_list.html",args)



##############################################for  Subscribing a Author ##############################################
@login_required
def user_subscribe_author(request):
	if request.method =='GET':
		##################################################################################################
		################################ from AdminPost Model #####################################
		delhi_shades_event = AdminPost.objects.all().filter(blog_category='Events',blog_published_status=True).order_by('-id')[0:4]
		delhi_diary = AdminPost.objects.all().filter(blog_category='Delhi Diary',blog_published_status=True).order_by('-id')[0:4]
		delhi_history = AdminPost.objects.all().filter(blog_category='History',blog_published_status=True).order_by('-id')[0:4]
		delhi_places = AdminPost.objects.all().filter(blog_category='Places',blog_published_status=True).order_by('-id')[0:4]
		delhi_architecture = AdminPost.objects.all().filter(blog_category='Architecture',blog_published_status=True).order_by('-id')[0:4]
		################################ from Blog Model ##########################################
		##################################################################################################
		######################### For Side panel add in every page #######################################
		recent_data = Blog.objects.all().filter(blog_published_status=True).order_by('-id')[0:4]
		popular_posts = Blog.objects.all().order_by('-id')[0:4]
		delhi_shades_count = Blog.objects.all().filter(blog_category='Delhi Shades',blog_published_status=True).count()
		fashion_count = Blog.objects.all().filter(blog_category='Fashion',blog_published_status=True).count()
		food_count = Blog.objects.all().filter(blog_category='Food',blog_published_status=True).count()
		travel_count = Blog.objects.all().filter(blog_category='Travel',blog_published_status=True).count()
		healthfitness_count = Blog.objects.all().filter(blog_category='Health & Fitness',blog_published_status=True).count()
		shopping_count = Blog.objects.all().filter(blog_category='Shopping',blog_published_status=True).count()
		technology_count = Blog.objects.all().filter(blog_category='Technology',blog_published_status=True).count()
		education_count = Blog.objects.all().filter(blog_category='Education',blog_published_status=True).count()
		social_count = Blog.objects.all().filter(blog_category='Social Welfare',blog_published_status=True).count()
		args={
		  'subscribe_author': SubscriptionForm(),
		  'delhi_shades_event':delhi_shades_event,
		  'delhi_shades':delhi_shades,
		  'delhi_diary':delhi_diary,
		  'delhi_history':delhi_history,
		  'delhi_architecture':delhi_architecture,
		  'delhi_places':delhi_places,
		  'recent_data':recent_data,
		  'popular_posts':popular_posts,
		  'delhi_shades_count':delhi_shades_count,
		  'fashion_count':fashion_count,
		  'food_count':food_count,
		  'travel_count':travel_count,
		  'healthfitness_count':healthfitness_count,
		  'shopping_count':shopping_count,
		  'technology_count':technology_count,
		  'education_count':education_count,
		  'social_count':social_count,
		  }
		return render(request,'HomePage/test.html', args)
	else:
		subscribe_author = SubscriptionForm(request.POST)
		form = subscribe_author.save(commit=False) # user ForeignKey is blank here raise error
		form.creator = request.user # add ForeignKey user name
		form.save() # now Add to database
		return redirect('user_profile')
