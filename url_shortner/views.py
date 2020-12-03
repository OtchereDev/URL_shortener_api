from django.shortcuts import render,HttpResponse,HttpResponseRedirect,Http404
from api.models import Shortener
from django.http import HttpResponse, HttpResponseNotFound

connectors=['http://', 'https://', 'ftp://', 'ftps://',
            'http:', 'https:', 'ftp:', 'ftps:',]



def redirector(request,pk):
    connect_url='localhost:8000/'+pk
    try:
        
        redirect_url = Shortener.objects.filter(shortened_link=connect_url).values('original_link').first()
    
        redirect_url=redirect_url['original_link']

    except (AttributeError, TypeError):
        # return HttpResponseNotFound("<h1>Page not found</h1>")
        return render(request,'error.html')
        # raise Http404
    if redirect_url.startswith(tuple(connectors)):
        return HttpResponseRedirect(''+redirect_url)
       
    else:
        return HttpResponseRedirect('https://'+redirect_url)
        
        