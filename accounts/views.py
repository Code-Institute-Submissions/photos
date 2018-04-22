from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth, messages
from blog.models import Post


def login(request):
    redirect_to = request.GET.get('next', 'home')
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))
    
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have sucessfully logged in")
                return redirect(redirect_to)
            else:
                form.add_error(None, "Your username or password was not recognised")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', { 'form': form })
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have sucessfully logged out")
    return redirect(request.GET.get('next', 'home'))
    
@login_required()
def profile(request):
    posts = Post.objects.all()
    my_posts = []
    for post in posts:
        if post.author == request.user:
            my_posts.append(post)
    return render(request, 'accounts/profile.html', {'my_posts': my_posts})
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('profile')

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})  
    
    