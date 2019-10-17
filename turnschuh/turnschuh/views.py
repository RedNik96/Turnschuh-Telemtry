import os
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from models import TransferFile
from zipfile import ZipFile 
from django.conf import settings
from wsgiref.util import FileWrapper
from django.views import View
from .models import TransferFile


def index(request):

    latest_question_list = [1,2,3,4]
    template = loader.get_template('turnschuh/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def upload(request):
    if request.method == 'POST':
        # zip erst
        # 

        print(request.FILES)
        print('---------- > {}'.format(request.FILES.getlist('files')))
        zipFiles(request.FILES.getlist('files'))
        transFile = TransferFile()
        transFile.description = request.description
#        transfile.path = 
    return render(request, 'turnschuh/upload.html', {
    })

def zipFiles(incfiles):                         
    print(incfiles)
    with ZipFile('my_python_files.zip','w') as zip: 
        # writing each file one by one 
        for file in incfiles: 
            print(file)
            zip.write(file.temporary_file_path()) 
    
  


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('index'))
        else:
            return render(request, 'turnschuh/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            ctx = {
                'error': True,
                'username': username
            }
            return render(request, 'turnschuh/login.html', ctx)


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))
    


def abfrage(request):
    latest_list = TransferFile.objects.order_by(('-transferTime'))[:5]
    template = loader.get_template('turnschuh/index.html')
    context = {
        'latest_list': latest_list,
    }
    return HttpResponse(template.render(context, request))



def filedownload(request):
        down = request.POST['down']

        mydownfile= os.path.join(settings.MEDIA_ROOT,down)    
        print(mydownfile)
        response = HttpResponse(FileWrapper(open(mydownfile,"rb")), content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=down'
        return response

def delete(request):
        deleteid = request.POST['delete']
        TransferFile.objects.filter(id=deleteid).delete()
        return redirect(reverse('abfrage'))

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
        
     

