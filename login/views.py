from django.shortcuts import render
from .forms import LoginForm, RegisterForm, ImageForm, ContactForm
from .models import Login, Register, Image, Contact
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import keras
from keras.preprocessing import image
import numpy as np
global graph, model



def register(request):
    a=[]
    if request.POST:
        registerForm=RegisterForm(request.POST)
        if registerForm.is_valid():
            a = Register.objects.all()
            for i in range(len(a)):
                if str(a[i]) == str(registerForm.cleaned_data['username']):
                    return HttpResponse("Username is already used")
            else:
                reg=registerForm.save()
                return HttpResponseRedirect('/login')
        else:
            print(registerForm.errors)
    else:
        registerForm=RegisterForm()
        return render(request, 'register.html', {'registerForm': registerForm})
    #contactForm = ContactForm()
    #return render(request, 'contact.html', {'contactForm': contactForm})




def login(request):
    a=[]
    if request.POST:
        loginForm=LoginForm(request.POST)
        if loginForm.is_valid():
            #log=loginForm.save()
            a=Register.objects.all()
            for i in Register.objects.all():
                if str(i.username)==str(loginForm.cleaned_data['username']) and str(i.password)== str(loginForm.cleaned_data['password']):
                    return HttpResponseRedirect('/img')
            else:
                return HttpResponse("You are not registered")
        else:
            print(loginForm.errors)
    else:
        loginForm=LoginForm()
        return render(request, 'login.html', {'loginForm': loginForm})
    #contactForm = ContactForm()
    #return render(request, 'contact.html', {'contactForm': contactForm})

prediction=''


def img(request):
    if request.POST:
        imgForm=ImageForm(request.POST, request.FILES)
        if imgForm.is_valid():
            newimg=Image(imgfile=request.FILES['imgfile'])
            newimg.save()
            imgfile = request.FILES['imgfile']
            name = imgfile.name
            h5_model = keras.models.load_model('login/xray_model.h5')
            test = image.load_img('images/' + name, target_size=(64, 64))
            test = image.img_to_array(test)
            test = np.expand_dims(test, axis=0)
            h5_prediction = h5_model.predict(test)
            print(h5_prediction)
            if h5_prediction[0][0]>=0.5:
                prediction='No'
                print(prediction)
                return HttpResponseRedirect('/contact')
            elif h5_prediction[0][0]==0:
                return HttpResponse("Not selected Correct Image")
            else:
                prediction='Yes'
                print(prediction)
                return HttpResponseRedirect('/contact')




    else:
        imgForm = ImageForm()
        return render(request, 'img.html', {'imgForm': imgForm})
    #contactForm = ContactForm()
    #return render(request, 'contact.html', {'contactForm': contactForm})



def contact(request):
    pred=''
    if prediction == 'No':
        lcondition = 'Infected'
        pred='YES'
    else:
        lcondition = 'Normal'
        pred='NO'
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your responce recorded")
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form, 'infound': pred, 'lcondition': lcondition})


