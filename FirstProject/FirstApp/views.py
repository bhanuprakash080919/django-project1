from django.shortcuts import render
from django.http import HttpResponse;
# Create your views here.
#single app multiple views
def show(request):
    x=''' <h1>Hello user.....! 
    welcome to django... <br> <br/>
    </h1>
    '''
    return HttpResponse(x)
def display(request):
    ss="<h2>Hello user.....!</h2><hr color=red width=90%/> <h2>good morning user</h2><hr color=brown width=80% />"
    return HttpResponse(ss)