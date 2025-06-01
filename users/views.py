from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from .forms import ProfileUpdateForm
from .forms import SignUpForm, LoginForm
from .models import Profile

# Create your views here.
def register_page(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list")
    else:
        form = SignUpForm()
    return render(request,'users/register.html', { "form": form })

def login_page(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
    else:
        form = LoginForm()
    return render(request,'users/login.html', { "form": form })

def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")

class FollowersView(View):
    def get(self, request, username):
        # Get the profile based on the username
        profile = Profile.objects.get(user__username=username)

        # Get all users who are following this profile
        followers = Profile.objects.filter(following=profile)  # Get profiles where the current profile is in the following field

        return render(request, 'users/followers_list.html', {'profile': profile, 'followers': followers})

class FollowingView(View):
    def get(self, request, username):
        # Get the profile based on the username
        profile = Profile.objects.get(user__username=username)

        # Get all users that this profile is following
        following = profile.following.all()  # Accessing the many-to-many relationship directly

        return render(request, 'users/following_list.html', {'profile': profile, 'following': following})

@login_required
def profile_page(request):
    # Handle profile update form submission
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    user = request.user
    profile = user.profile

    # Get all posts created by this user
    user_posts = user.posts.all()

    # Get all followers (Profiles that follow this user)
    followers = Profile.objects.filter(following=profile)

    context = {
        'user': user,
        'posts': user_posts,
        'form': form,
        'profile': profile,
        'followers': followers,  # <-- Pass this to the template
    }

    return render(request, 'users/profile.html', context)

@login_required
def toggle_follow_user(request, username):
    target_user = get_object_or_404(User, username=username)
    profile = request.user.profile
    is_following = request.user.profile.following.filter(user=target_user).exists()
    
    if request.method == "POST":
        if is_following:
            profile.following.remove(target_user.profile)
        else:
            profile.following.add(target_user.profile)
        is_following = request.user.profile.following.filter(user=target_user).exists()

    # Render updated button
    html = render_to_string(
        "users/follow_button.html",
        {
        "target": target_user.profile,
        "is_following": is_following,
        },
        request = request
    )

    return JsonResponse({"html": html})

@login_required
def rmv_follower(request, username):
    follower = get_object_or_404(User, username=username)
    profile = request.user.profile
    
    if request.method == "POST":
        follower.profile.following.remove(profile)

    is_followed = follower.profile.following.filter(id=profile.id).exists()

    # Render updated button
    html = render_to_string(
        "users/rmv_follower_button.html", 
        {
        "target": follower.profile,
        "is_followed": is_followed,
        },
        request = request
    )

    return JsonResponse({"html": html})

@login_required
def profile_notes_page(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')  # Redirect to the profile page after upload
    else:
        form = ProfileUpdateForm(instance=request.user.profile)  # ← fixed here
        
    # Directly pass the user object instead of getting the username
    # Get a specific user
    user = request.user

    # Get all notess for that user
    user_notes = user.notes.all()
    return render(request, 'users/profilenotes.html', {'user': request.user, 'notes': user_notes, 'form': form, 'profile': request.user.profile})

@login_required
def follow_user(request, username):
    target_user = get_object_or_404(User, username=username)
    if request.user != target_user:
        request.user.profile.following.add(target_user.profile)
    return redirect('users:other_profile', username=target_user.username)

@login_required
def unfollow_user(request, username):
    target_user = get_object_or_404(User, username=username)
    if request.user != target_user:
        request.user.profile.following.remove(target_user.profile)
    return redirect('users:other_profile', username=target_user.username)

@login_required
def other_user_profile(request, username):
    target_user = get_object_or_404(User, username=username)
    target_profile = target_user.profile
    target_posts = target_user.posts.all()  # or `.notes.all()` if you're showing notes

    is_following = target_profile in request.user.profile.following.all()

    context = {
        'profile_user': target_user,
        'profile': target_profile,
        'posts': target_posts,
        'is_following': is_following,
    }
    return render(request, 'users/other_profile.html', context)