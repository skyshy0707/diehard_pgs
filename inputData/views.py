from .forms import CustomInputUserCreationForm as form_class
from .models import Input
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from . import testing


# Create your views here.
		
def upload_file(request):
	if request.method == 'POST':
		form = form_class(request.POST, request.FILES)
		if form.is_valid():
			filename = request.FILES['file'].name
			form.save()
			ID = Input.objects.last().id
			testing.test(ID, filename)
			
			return HttpResponseRedirect('/results/')
		else:
			return self.form_invalid(form)
	else:
		form = form_class()
	return render(request, 'home.html', {'form': form})
			
