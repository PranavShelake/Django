from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from account.models import account
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate, logout,login as auth_login

def login_page(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            messages.error(request, 'All fields are required.')
            return redirect('login_page')

        user = authenticate(request, username=email, password=password)
        print(user)  
        if user is not None:
            auth_login(request, user)
            return redirect('success')
        else:
            messages.error(request, 'Invalid Email or Password.')
            return redirect('login_page')
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        # Get form data from POST request
        data = request.POST
        email = data.get('email')
        first_name = data.get('fname')
        password = data.get('password')
        security_key = data.get('key')
        
        # Validate form data
        if not email or not first_name or not password or not security_key:
            messages.error(request, 'All fields are required.')
            return redirect('register')  # Redirect back to the registration page
        
        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken.')
            return redirect('register')  # Redirect back to the registration page
        
        try:
            # Create a new User object
            user = User.objects.create_user(username=email, email=email, first_name=first_name)
            user.set_password(password)
            user.save()

            # Create an Account object associated with the new User
            account.objects.create(user=user, security_key=security_key)
            
            # Optionally, you can log in the user after registration
            # auth_login(request, user)
            
            # Redirect to a success page or login page
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login_page')  # Replace 'login_page' with your actual login URL name
        
        except Exception as e:
            messages.error(request, f'Error occurred during registration: {str(e)}')
            return redirect('register')  # Redirect back to the registration page
    
    # If GET request, render the registration form
    return render(request, 'register.html')


def reset_password(request, id):
    if request.method == 'POST':
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            try:
                user = User.objects.get(id=id)
                user.set_password(password)
                user.save()
                messages.success(request, 'Password reset successfully.')
                return redirect('login_page')  # Replace 'success' with your actual success URL name
            except User.DoesNotExist:
                messages.error(request, 'User does not exist.')
                return redirect('login_page')  # Redirect to login page or handle as needed
        else:
            messages.error(request, 'Passwords does not match.')
            return redirect('reset_password', id=id)  # Redirect back to the reset password form with user id

    return render(request, 'reset_password.html')


def verification(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        security_key = request.POST.get('key')

        if not email or not security_key:
            messages.error(request, 'All fields are required.')
            return redirect('verification')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Invalid email.')
            return redirect('verification')
        
        try:
            user_account = account.objects.get(user=user)
            if user_account.security_key == security_key:
                # Redirect to reset password page with user id
                return redirect('reset_password', id=user.id)
            else:
                messages.error(request, 'Invalid security key.')
                return redirect('verification')
        except account.DoesNotExist:    
            messages.error(request, 'Account does not exist for this user.')
            return redirect('verification')

    return render(request, 'verification.html')


def logout_page(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('/login_page/')