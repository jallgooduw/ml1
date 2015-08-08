from django.shortcuts import render
from .models import URLExp

# Create your views here.

def url_list(request):
	urls = URLExp.objects.all()
	return render(request, 'urlexpander/url_list.html', {'urls': urls})

