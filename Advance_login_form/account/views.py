from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from account.models import account
from django.contrib import messages
from .email import sent_mail
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, logout,login as auth_login
import random
# Create your views here.

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

 
def verify_email(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        gen_otp = request.session.get('gen_otp')  # Retrieve OTP from session
        
        if otp == str(gen_otp):
            # Retrieve user data from the session
            first_name = request.session.get('first_name')
            email = request.session.get('email')
            hashed_password = request.session.get('hashed_password')
            security_key = request.session.get('security_key')
            
            # Clear the session data to avoid keeping sensitive info
            request.session.flush()

            # Create and save the user with the hashed password
            user = User.objects.create_user(username=email, email=email, first_name=first_name)
            user.password = hashed_password
            user.save()

            # Create the associated account
            account.objects.create(user=user, security_key=security_key)

            messages.success(request, 'Registration successful. Please login.')
            return redirect('login_page')
        else:
            messages.error(request, 'OTP is incorrect.')
            return redirect('verify_email')
    
    return render(request, 'verify_email.html')


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
            # Generate OTP
            gen_otp = random.randint(1000, 9999)
            
            # Send OTP via email
            sent_mail(first_name, email, gen_otp)
            
            # Hash the password before storing in the session
            hashed_password = make_password(password)
            
            # Store user data and OTP in the session securely
            request.session['first_name'] = first_name
            request.session['email'] = email
            request.session['hashed_password'] = hashed_password
            request.session['security_key'] = security_key
            request.session['gen_otp'] = gen_otp
            messages.success(request, 'OTP sended to your email')
            return redirect('verify_email')
        
        except Exception as e:
            # messages.error(request, f'Invalid email')
            messages.error(request, f'Error occurred during registration: {str(e)}')
            return redirect('register')  # Redirect back to the registration page
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