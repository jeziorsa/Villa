from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from villaproject.main.forms import RegistrationForm

def dashboard(request):
    render(request, 'dashboard.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return render(request, 'sign_up.html')
            print form
    else:
        form = RegistrationForm()

    return render(request, 'sign_up.html', {
        'form':form,
        })

def login(request):

    if request.method == 'POST':
        print 'przed'
        c = {}
        c.update(csrf(request))
        username = request.POST['username']
        password = request.POST['password']
        print username
        print password

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                #login(request)
                print 'jest dobrze'
                return render(request, 'dashboard.html')
        else:
            print 'jest zle'
            return render(request, 'base.html')

def home(request):
    return render(request, 'base.html')



def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            print 'jest dobrze'
            # Return a 'disabled account' error message
    else:
        print 'jest'
        # Return an 'invalid login' error message.


def logout_view(request):
    logout(request)
    return render( request, 'base.html')