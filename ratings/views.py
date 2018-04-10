from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ReviewForm
from photos.models import Photo

# Create your views here.
def add_a_rating(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    
    photo_id = int(request.POST['photo'])
    print(photo_id)
    photo = get_object_or_404(Photo, pk=photo_id)
    
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.reviewer = request.user
        review.photo = photo
        review.save()
        return redirect(reverse('photo_detail', args=(photo_id,)))
        
        
