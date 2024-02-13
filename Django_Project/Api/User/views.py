from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages

def register(request):
    if(request.method=='POST'):
        print(request.POST)
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # Access cleaned data after validation
            messages.success(request, f'Account created for {username}')
            return redirect('login')
        else:
            return HttpResponse('Some Error Occured')
    else:
        form=UserCreationForm()
        return render(request,'user/registration.html',{'form':form})


def login(request):
    return 'user/login.html'