from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from Account.forms import LoginForm
from django.contrib.auth.views import LoginView


# Create your views here.
def SignupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('/')


class CustomLoginView(LoginView):
    template_name = "login.html"  # your template
    from_class = LoginForm
    redirect_authenticated_user = True
