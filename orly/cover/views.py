from django.http import HttpResponse
from django.shortcuts import render, redirect
from PIL import Image
from .forms import CoverForm

def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            return redirect('cover:index')
    else:
        form = CoverForm
    return render(request, 'cover/index.html', {
        'form': form,
    })

def image_generator(request):
    im = Image.new('RGB', (256, 256))
    response = HttpResponse()
    im.save(response, format='JPEG')
    return res ponse