from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, EditPostForm
from django.utils import timezone
from django.http import HttpResponseForbidden

# Create your views here.

    
def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, id):
    post=get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})

    
def create_post(request):
    if request.user.is_authenticated == False:
        print("Nice try")
        return HttpResponseForbidden()
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        message = form.save(commit=False)
        message.author = request.user
        message.save()
        return redirect('post_list')
    else:
        form = PostForm()
    
    return render(request, "blog/new_post.html", { 'form': form })
    
    
def edit_post(request, id):
    item = get_object_or_404(Post, pk=id)
    
    if item.author != request.user:
        print("Nice try")
        return HttpResponseForbidden()
    if request.method == "POST":
        print("It's a post")
        form = EditPostForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        print("It's a get")
    
    form = EditPostForm(instance=item)
    return render(request, 'blog/edit_post.html', {'form': form})


def like_post(request, id):
    if request.user.is_authenticated == False:
        return HttpResponseForbidden()
    post = get_object_or_404(Post, pk=id)
    post.likes += 1
    post.save()
    return redirect("post_list")     
    
def delete_post(request, id):
    item = get_object_or_404(Post, pk=id)
    if item.author != request.user:
        return HttpResponseForbidden()
    item.delete()
    return redirect("post_list")
    
    
def search_posts(request):
    match = request.GET.get('match')
    posts = Post.objects.filter(content__icontains=request.GET['query'])
    return render(request, "blog/post_list.html", {"posts": posts})