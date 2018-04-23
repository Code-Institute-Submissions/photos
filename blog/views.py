from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from .forms import PostForm, EditPostForm, LikeForm
from django.utils import timezone
from django.http import HttpResponseForbidden
from django.contrib import auth, messages
    
def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, id):
    post=get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required()
def create_post(request):
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        message = form.save(commit=False)
        message.author = request.user
        message.save()
        return redirect('post_list')
    else:
        form = PostForm()
    return render(request, "blog/new_post.html", { 'form': form })
    
@login_required()
def edit_post(request, id):
    item = get_object_or_404(Post, pk=id)
    if item.author != request.user:
        print("You can't edit other users posts.")
        return HttpResponseForbidden()
    if request.method == "POST":
        form = EditPostForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        print("It's a get")
    
    form = EditPostForm(instance=item)
    return render(request, 'blog/edit_post.html', {'form': form})

@login_required()
def like_post(request, id):
    post = get_object_or_404(Post, pk=id)
    
    print(post)
    
    liked = False
    likes = Like.objects.all()
    for like in likes:
        if like.post == post and like.reviewer == request.user:
            liked = True
            
    form = LikeForm(request.POST)  
    if form.is_valid():
        this_like = form.save(commit=False)
        if request.user == post.author:
            messages.error(request, "You can not like your own post")
        elif liked == False:
            this_like.reviewer = request.user
            this_like.post = post
            post.likes += 1
            post.save()
            this_like.save()
        else:
            messages.error(request, "You have already liked this post")
    return redirect(reverse('post_detail', args=(post.id,)))     
  
@login_required()  
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