from django.contrib import admin
from django.urls import path
from HomePage import views

app_name ='HomePage'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('view_user_info/', views.view_user_info, name='view_user_info'),
    path('blog/author/add/new/post/', views.addblog, name='addblog'),
    path('blog/author/all/posts/<int:blog_pk>/delhi_shades', views.view_user_blog, name='detail_blog'),
    path('blog/author/all/posts/list_blog/', views.list_view_blog, name='list_blog'),
    path('blog/author/posts/update/<int:blog_pk>/', views.update_view_blog, name='update_blog'),
    path('blog/author/posts/delete/<int:blog_pk>/delete', views.delete_view_blog, name='delete_blog'),
    path('author/profile/<int:blog_pk>/', views.author_profile_view, name='user_profile'),
    path('test/', views.test, name='test'),

    #****************************For Adding in User Blog by Users ***************************************#

    #******Delhi Shades Blog*******#
    path('blog/delhi_shades/', views.delhi_shades, name='delhi_shades_list'),
    #******fashion Blog*******#
    path('blog/fashion_blog/', views.fashion_blog, name='fashion_blog_list'),
    #******For User food Blog*******#
    path('blog/food_blog/', views.food_blog, name='food_blog_list'),
    #******For User travel Blog*******#
    path('blog/travel_blog/', views.travel_blog, name='travel_blog_list'),
    #******For User health Blog*******#
    path('blog/health_blog/', views.health_blog, name='health_blog_list'),
    #******For User social Blog*******#
    path('blog/social_blog/', views.social_blog, name='social_blog_list'),
      #******For Event Blog*******#
    path('blog/event_and_entertainment/', views.event_blog, name='event_blog_list'),
    #******For User Shopping Blog*******#
    path('blog/shopping_blog/', views.shopping_blog, name='shopping_blog_list'),
    path('create_account/', views.create_account, name='create_account'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('about_us/', views.contact, name='about_us'),
 
#****************************For Admin list ***************************************#  
    path('blog/delhishades/', views.admin_post_list, name='admin_post_list'),
#****************************For Admin Detail ***************************************#  
    path('blog/delhishades/<int:blog_pk>', views.admin_post_detail, name='admin_post_detail'),

#**************************** Delhi Events List ***************************************#  
    path('blog/delhishades/delhi_events/', views.delhi_events, name='delhi_events_list'),
#**************************** Delhi Diary List ***************************************#  
    path('blog/delhishades/delhi_diary/', views.delhi_diary, name='delhi_diary_list'),
#**************************** Delhi History List ***************************************#  
    path('blog/delhishades/delhi_history/', views.delhi_history, name='delhi_history_list'),
#**************************** Delhi Architecture List ***************************************#  
    path('blog/delhishades/delhi_architecture/', views.delhi_architecture, name='delhi_architecture_list'),
#**************************** Delhi Places List ***************************************#  
    path('blog/delhishades/delhi_places/', views.delhi_places, name='delhi_places_list'),
#**************************** Author Profile List  ***************************************#  
    path('blog/author/author_profile_list/', views.author_profile_list, name='author_profile_list'),
#**************************** Author Detail List  ***************************************#  
    path('home/blog/author/<int:author_pk>/', views.author_profile_detail, name='author_profile_detail'),
################################### For Author unpublished blogs #######################################
    path('blog/author/author_unpublished_list/', views.author_unpublished_list, name='author_unpublished_list'),
################################### For Disclaimer and policy #######################################
    path('blog/author/disclaimer_and_policy/', views.disclaimer_and_policy, name='disclaimer_and_policy'),
################################### For user_profile_info_list #######################################
    path('blog/author/user_profile_info/', views.user_profile_info_list, name='user_profile_info_list'),
################################### For user_profile_info_list #######################################
    path('blog/author/user_profile_info_detail/<int:author_pk>', views.user_profile_info_detail, name='user_profile_info_detail'),
################################### For user_profile_info_list #######################################
    path('blog/author/user_profile_info_update/<int:author_pk>', views.user_profile_info_update, name='user_profile_info_update'),
################################### For user_subscription_list #######################################
    path('blog/author/following/<int:author_pk>/', views.user_subscription_list, name='user_subscription_list'),
################################### For user_subscription_list #######################################
    path('blog/author/followers/<int:author_pk>/', views.user_subscriber_list, name='user_subscriber_list'),
################################### For user_subscribe author  #######################################
    path('blog/author/user_subscribe_author/', views.user_subscribe_author, name='user_subscribe_author'),
################################### For author_unsubscribe   #######################################
    path('blog/author/unfollowers/<int:author_pk>/delete', views.author_unfollow, name='author_unfollow'),

]
