from django.shortcuts import render, redirect
from django.contrib import messages
from .email import sent_mail
def home(request):
    if request.method == "POST":
        data = request.POST

        name = data.get('name')
        gmail = data.get('gmail')
        message = data.get('message')
        file = request.FILES.get('file')
        
        sent_mail(name, gmail, message, file)
        
        messages.success(request, 'Your message has been sent successfully!')

        return redirect('home')
    
    return render(request, 'index.html')
