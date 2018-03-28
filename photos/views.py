from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from ratings.forms import ReviewForm
# Create your views here.

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, "photos/photo_list.html", {'photos': photos})    
    
def photo_detail(request, id):
    photos = get_object_or_404(Photo, pk=id)
    form = ReviewForm()
    return render(request, "photos/photo_detail.html", {'photos': photos, 'review_form': form})