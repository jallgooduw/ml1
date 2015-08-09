from django.shortcuts import render
from .models import URLExp
from django.shortcuts  import redirect 
from bs4 import BeautifulSoup #not sure if correct
from requests import request #not sure if correct

# Create your views here.

def url_list(request):
	urls = URLExp.objects.all()
	return render(request, 'urlexpander/url_list.html', {'urls': urls})


def url_submit(request):
	if request.method == "POST":
		form = SubmitForm(request.POST)
		if form.is_valid(): 
			post = form.save(commit=False)
			post.save() #need to save submitted URL to shorturl in db
			processor(form) #need to pass submitted URL to proces (get status, destination, title)
			return redirect('urlexpander.views.url_list', pk=post.pk)
		else:
			return render(request, 'urlexpander/url_submit.html', {'form': form})
def processor(str):
	url = str
	r = requests.get(url)
	

#def url_submit(request): #pseudo
#	urls = URLExp.object.shorturl()
#	r = requests.get(url here from form)
#	r.status_code = POST to database at httpstatus
#	r.url = POST to database at finaldestination
#	r.text
#	parser(r.text)
	
#	return render(request, 'urlexpander/url_submit.html')

#def parser(r.text): #pseudo
#	soup = BeautifulSoup(r.text, 'html.parser')
#	return soup.title


# r = requests.get(URLExp.objects.shorturl)
# r = requests.get('url from URLExp.shorturl')
# r.status_code = URLExp.httpstat
#r.url = URLExp.finaldestination
#r.text
#from bs4 import BeautifulSoup
#
