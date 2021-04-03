from django.urls import path
from . import views 
urlpatterns = [
        #main paig
        path("", views.index, name="index"),
        #groupe list page
        path("groups",views.groups_list, name="list"),
        path('group/<str:slug>/',views.detail_group, name="detail_group_url"),
        #user page , list post , vews and edit post
        path('<str:user>/',views.profile,name='profile'),
        path('<str:username>/<int:post_id>/',views.post_views,name='post'),
        path(
            '<str:username>/<int:post_id>/edit/',
            views.post_edit,
            name='post_edit'),
        #create post 
        path("create",views.CreatePost.as_view(), name="create_post_url"),
    ]



