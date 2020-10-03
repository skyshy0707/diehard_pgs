from django.shortcuts import render

from django.http import Http404
from .models import Results
from inputData.models import Input
from . import parse_res
from diehard.settings import BASE_DIR
import os
import json
from django.shortcuts import redirect

# Create your views here.


def results(req):
	inps = Input.objects.all()
	return render(req, 'results.html', {'results': inps})
	
	

def result(req, res_id):
	inp = Input.objects.get(pk = res_id)
	path = os.path.join(BASE_DIR, 'uploads\\' + str(res_id) + '\\t.txt')
	p_values = parse_res.main(path)
	res = Results(generator = inp, pvalues = p_values)
	print("pvalues", p_values, "JSON: ", json.dumps(p_values))
	res.save(using = 'results')
	return render(req, 'result.html', {'res': res})
	'''try:
		inp = Input.objects.get(pk = res_id)
		path = os.path.join(BASE_DIR, 'uploads\\' + str(res_id) + '\\t.txt')
		p_values = parse_res.main(path)
		res = Results(generator = inp, pvalues = p_values)
		res.save(using = 'results')'''
	'''except Results.DoesNotExist:
		raise Http404
	return render(req, 'result.html', {'res': res})'''
	
