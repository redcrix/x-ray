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
                    return render(request, 'register.html', {'registerForm': registerForm, 'result': 'username is already registered'})
            else:
                reg=registerForm.save()
                return HttpResponseRedirect('/login')
        else:
            print(registerForm.errors)
    else:
        registerForm=RegisterForm()
        return render(request, 'register.html', {'registerForm': registerForm})




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
                return render(request, 'login.html', {'loginForm': loginForm, 'result': 'You are not registered or check your password'})
        else:
            print(loginForm.errors)
    else:
        loginForm=LoginForm()
        return render(request, 'login.html', {'loginForm': loginForm})




def img(request):
    prediction = ''

    dict = {0: 'Atelectasis', 1: 'Cardiomegaly', 2: 'Consolidation', 3: 'Edema', 4: 'Effusion', 5: 'Emphysema',
            6: 'Fibrosis', 7: 'Hernia', 8: 'Infiltration', 9: 'Mass', 10: 'No Finding', 11: 'Nodule',
            12: 'Pleural_Thickening', 13: 'Pneumonia', 14: 'Pneumothorax'}

    condition = ''
    des = ''
    fp = ''

    if request.POST:
        imgForm=ImageForm(request.POST, request.FILES)
        if imgForm.is_valid():
            newimg=Image(imgfile=request.FILES['imgfile'])
            newimg.save()
            imgfile = request.FILES['imgfile']
            name = imgfile.name
            request.session['name'] = name
            '''
                        h5_model = keras.models.load_model('login/xray_model.h5')
                        test = image.load_img('images/' + name, target_size=(64, 64))
                        test = image.img_to_array(test)
                        test = np.expand_dims(test, axis=0)
                        h5_prediction = h5_model.predict(test)
                        print(h5_prediction)

                        for i in range(len(h5_prediction[0])):
                            if h5_prediction[0][i]>0:
                                prediction='Yes'
                                des=dict[i]
                                condition='Infected'
                                fp = 'Contact to Doctor'
                                print(condition)
                                print(prediction)
                                request.session['data'] = {'infound': prediction, 'lcondition': condition, 'des': des, 'fp':fp}
                                return HttpResponseRedirect('/contact')
                            elif h5_prediction[0].sum()==0:
                                return render(request, 'img.html', {'imgForm': imgForm , 'result': "Selected image is not correct"})
                        else:
                            prediction='NO'
                            des = '-'
                            condition = 'Normal'
                            fp = '-'
                            print(prediction)
                            request.session['data'] = {'infound': prediction, 'lcondition': condition, 'des': des, 'fp':fp}
                            return HttpResponseRedirect('/contact')
            '''
            return HttpResponseRedirect('/contact')


    else:
        imgForm = ImageForm()
        return render(request, 'img.html', {'imgForm': imgForm})




def contact(request):

    prediction = ''

    dict = {0: 'Atelectasis', 1: 'Cardiomegaly', 2: 'Consolidation', 3: 'Edema', 4: 'Effusion', 5: 'Emphysema',
            6: 'Fibrosis', 7: 'Hernia', 8: 'Infiltration', 9: 'Mass', 10: 'No Finding', 11: 'Nodule',
            12: 'Pleural_Thickening', 13: 'Pneumonia', 14: 'Pneumothorax'}

    condition = ''
    des=''
    fp=''

    name = request.session.get('name')
    h5_model = keras.models.load_model('login/xray_model.h5')
    test = image.load_img('images/' + name, target_size=(64, 64))
    test = image.img_to_array(test)
    test = np.expand_dims(test, axis=0)
    h5_prediction = h5_model.predict(test)
    print(h5_prediction)

    for i in range(len(h5_prediction[0])):
        if h5_prediction[0][i] > 0:
            prediction = 'Yes'
            des = dict[i]
            condition='Infected'
            fp = 'Contact to Doctor'
            break
            #print(condition)
            #print(prediction)

        else:
            prediction = 'No'
            des='No'
            condition='Normal'
            fp='-'
            #print(prediction)


    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()



            return HttpResponse("Your responce recorded")
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form, 'infound': prediction, 'lcondition': condition, 'des': des, 'fp':fp})


