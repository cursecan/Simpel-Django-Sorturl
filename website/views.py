from django.shortcuts import render, redirect
from django.http import Http404
from .forms import WebsiteForm
from .models import Website


def index(request):
    form = WebsiteForm(request.POST or None)

    obj = None
    if request.POST:
        if form.is_valid():
            obj = form.save()


    websites = Website.objects.all()

    return render(request, 'website/index.html', {'form': form, 'website': websites, 'obj': obj})


def detail(request, code):
    try :
        obj = Website.objects.get(code=code)
        return redirect(obj.site_url)

    except:
        raise Http404("Data not found")