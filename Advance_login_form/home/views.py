from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login_page/')
def success(request):
    return render(request, 'success.html')  