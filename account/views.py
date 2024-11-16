from django.http import HttpResponse ,JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm , UserEditForm, ProfileEditForm ,PlayerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Player
from django.views.generic import ListView, DetailView
from matches.models import Match,News

from .forms import UserRegistrationForm


from django.contrib.auth.decorators import login_required, user_passes_test


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            # Log the user in after registration
            login(request, new_user)
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
        
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})




@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated '\
            'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})




@login_required
def dashboard(request):
    players = Player.objects.all()
    profiles = Profile.objects.all()
    total_profiles = profiles.count()
    total_players = players.count()

    total_matches = Match.objects.count()
    total_news = News.objects.count()

    # Example data for a pie chart
    chart_data = {
        'labels': ['Players', 'Matchs', 'News','Profiles'],
        'data': [total_players, total_matches, total_news,total_profiles],
        'backgroundColor': ['#36A2EB', '#FF6384', '#FFCE56','#0529C92A'],
    }
    bar_chart_data = {
        'labels': ['Players', 'Matchs', 'News','Profiles'],
        'data': [total_players, total_matches, total_news ,total_profiles],
        'backgroundColor': ['#0F8A04', '#CCBF0B', '#FF5C56','#0529C92A'],
    }

    return render(
        request,
        'account/dashboard.html',
        {
            'section': 'dashboard',
            'total_profiles':total_profiles,
            'profile_players': players,
            'total_players': total_players,
            'total_matches': total_matches,
            'total_news': total_news,
            'chart_data': chart_data,
            'bar_chart_data': bar_chart_data,
        }
    )

#########



class PlayerListView(ListView):
    model = Player
    template_name = 'account/player_list.html'
    context_object_name = 'players'
    ordering = ['name']  
    def get_queryset(self):
        return Player.objects.all()


@login_required
def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'account/player_detail.html', {'player': player})

@user_passes_test(lambda u: u.is_superuser)
def player_add(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'account/player_edit.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def player_edit(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'account/player_edit.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def player_remove(request, pk):
    player = get_object_or_404(Player, pk=pk)
    player.delete()
    return redirect('player_list')

@login_required
def player_dashboard(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'account/player_dashboard.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('player_dashboard')
    else:
        form = ProfileEditForm(instance=user_profile)

    return render(request, 'account/edit_profile.html', {'form': form})