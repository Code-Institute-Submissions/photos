from django.shortcuts import render, get_object_or_404
from photos.models import Photo
from blog.models import Post


# Create your views here.
def home(request):
    photos = Photo.objects.all()
    top = get_object_or_404(Photo, pk=1)
    for p in photos:
        if p.id is None or p.average_rating is None:
            pass
        elif p.average_rating > top.average_rating:
            top = p
            
    posts = Post.objects.all()
    most_viewed = get_object_or_404(Post, pk=1)
    for p in posts:
        if p.id is None or p.views is None or p.views == 0:
            pass
        elif p.views > most_viewed.views:
            most_viewed = p
    return render(request, 'home/index.html', {"photos":photos, "top": top, "most_viewed": most_viewed})