from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .models import pdf

def home(request):
    pdfs = pdf.objects.all()
    return render(request, 'home.html', {
        'pdfs': pdfs
    })

# Create your views here.
def upload(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs =  FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)
        pdf.objects.create(title=name, content='', pdf=context['url'])
    return render(request, 'upload.html', context)

