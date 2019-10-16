from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from models import TransferFile
from zipfile import ZipFile 

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
    
  