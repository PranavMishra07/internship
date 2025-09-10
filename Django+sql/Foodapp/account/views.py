from django.shortcuts import render,HttpResponse,redirect
from .forms import User_Model_Form
from .models import Form_User

# Create your views here.

def Model_form(req):
    if req.method == "POST":
        form=User_Model_Form(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Submit")
        
    form=User_Model_Form()
    return render(req,"home.html",{"form":form})