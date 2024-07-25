from django.shortcuts import render,redirect
# Create your views here.

from home.models import Student

def data(request):
    data=Student.objects.all()
    context ={'student':data}
    return render(request, 'data.html',context)  


def delete_student(request,id):
    data=Student.objects.get(id=id)
    data.is_delete=True
    data.save()
    return redirect('/')