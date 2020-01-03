from django.shortcuts import render
from django.contrib.auth import authenticate, login
from home.forms import UserRegistrationForm, ProfileForm, UserForm, UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from home.models import Profile
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()

            return render(request, 'account/register_done.html', {'new_user': new_user})
        profile = Profile.objects.create(user=new_user)#add for edit
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

#add for edit
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'profile.html')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'home/profile_update.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


class ProfileView(DetailView):
    model = Profile    
    template_name = 'home/profile.html'

class ProfileListView(ListView):
    model = Profile
    form_class = ProfileForm
    template_name = 'home/profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Редактирование профиля:"
        return context

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'home/profile_update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

