'''
views doc string
'''
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from my_app.models import Customer
from my_app.forms import UserForm, UserProfileInfoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    '''
    index page
    '''
    return render(request, 'my_app/index.html')

@login_required
def customers(request):
    '''
    Customers list
    '''
    customer_list = Customer.objects.order_by('first_name')
    list_customer = {'customer_list': customer_list}
    return render(request, 'my_app/customer_list.html', context=list_customer)

def sign_up(request):
    '''
    New User Registration - Registration is required to be able to see all customers
    '''
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'my_app/sign_up.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print('someone tried to login and failed')
            print('username: {} and password {}'.format(username, password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'my_app/login.html', {})

def base(request):
    '''
    base page
    '''
    return render(request, 'my_app/base.html')

def need_login(request):
    return render(request, 'my_app/need_login.html')

@login_required
def user_logout(request):
    '''
    user logout
    '''
    logout(request)
    return HttpResponseRedirect(reverse('index'))
