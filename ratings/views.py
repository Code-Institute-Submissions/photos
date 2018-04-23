from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ReviewForm
from .models import Review
from photos.models import Photo
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def add_a_rating(request):
    photo_id = int(request.POST['photo'])
    photo = get_object_or_404(Photo, pk=photo_id)
    reviews = Review.objects.all()
    reviewed = False
    for review in reviews:
        if review.photo == photo and review.reviewer == request.user:
            reviewed = True
    
    form = ReviewForm(request.POST)
    if form.is_valid() and reviewed == False:
        review = form.save(commit=False)
        review.rating = int(request.POST['rating'])
        review.reviewer = request.user
        review.photo = photo
        review.save()
        return redirect(reverse('photo_detail', args=(photo_id,)))
    else:
        messages.error(request, "You have already reviewed this photo.")
        return redirect(reverse('photo_detail', args=(photo_id,)))
        
