from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('registration_success') 

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('registration_success')
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})


def get_user_profile(request):
    user = request.user
    data = {
        'username': user.username,
        'email': user.email,
        'date_of_birth': str(user.date_of_birth),
        'profile_image': user.profile_image.url if user.profile_image else None,
    }
    response = JsonResponse(data)
    response["Access-Control-Allow-Origin"] = "http://localhost:5173"
    response["Access-Control-Allow-Credentials"] = "true"
    return response