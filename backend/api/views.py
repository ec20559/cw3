from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm

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
            return redirect('profile')
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})