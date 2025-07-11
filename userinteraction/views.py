from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def userinteraction(request):
    return HttpResponse("<h1>hey i django server.</h1>")



@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile has been successfully updated')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})
