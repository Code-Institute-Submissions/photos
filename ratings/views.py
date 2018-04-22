from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ReviewForm
from photos.models import Photo
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def add_a_rating(request):
    photo_id = int(request.POST['photo'])
    photo = get_object_or_404(Photo, pk=photo_id)
    
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.reviewer = request.user
        review.photo = photo
        review.save()
        return redirect(reverse('photo_detail', args=(photo_id,)))
    else:
        messages.error(request, "Number should be between 1 and 5")
        return redirect(reverse('photo_detail', args=(photo_id,)))
        
