from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            
            return redirect('login')
    else:
        form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form})
