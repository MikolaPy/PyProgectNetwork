from django.views.generic import View
from django.shortcuts import render,redirect
from .forms import PostForm 
from django.core.paginator import Paginator
from .models import Post,Group,User

#main page ' ' 
def index(request):
    post_list = Post.objects.order_by("-pub_date").all()
    paginator = Paginator(post_list,10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
                request,
                'index.html',
                {"page":page,'paginator':paginator}
                )
def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'groups.html',{"names_groups":groups})

def detail_group(request,slug):
    related_group = Group.objects.get(slug=slug)
    posts = related_group.related_posts.all() 
    return render(request, 'groups_index.html',{"posts":posts})

class CreatePost(View):
    def get(self,request):
        form = PostForm()
        return render(request, "create_post.html",context = {"form":form})
    def post(self,request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect("/")
        return render(request, "create_post.html",context = {"form":bound_form})
        
def profile(request,user):
    user = User.objects.get(username = user)
    print('######')
    print(dir(user))
    posts=Post.objects.filter(author=user)
    return render(request,'profile.html',{'posts':posts})

def post_views():
    pass
def post_edit():
    pass 

