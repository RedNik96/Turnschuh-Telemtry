import os
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from wsgiref.util import FileWrapper


def index(request):

    latest_question_list = [1,2,3,4]
    template = loader.get_template('turnschuh/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


    # generate the file
    myfile= os.path.join(settings.MEDIA_ROOT,"uploads/dummy.zip")
    print(myfile)
    response = HttpResponse(FileWrapper(open(myfile,"rb")), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=dummy'
    return response