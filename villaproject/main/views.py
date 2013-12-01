from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf

def home(request):


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
            #login(request, user)
            # Redirect to a success page.
                print 'jest dobrze'
                return render( request, 'dashboard.html')
        else:
            print 'jest zle'
            # Return a 'disabled account' error message

        return render( request, 'base.html')

    else:
        return render( request, 'base.html')


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