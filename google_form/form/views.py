from django.http import HttpResponse
from django.http import Http404
# from django.template import loader
from django.shortcuts import render
from .models import Form

def index(request):
	all_forms = Form.objects.all()
	# html = ''
	# for forms in all_forms:
	# 	url = '/form/' + str(forms.id) + '/'
	# 	html += '<a href="' + url + '">' + forms.form_name + '</a><br>'
	# template = loader.get_template('form/index.html')

	# context = {'all_forms' : all_forms}
	# return HttpResponse(template.render(context,request))
	return render(request, 'form/index.html', {'all_forms' : all_forms})

def detail(request,form_id):
	# return HttpResponse("<h2>Details for form id:" + str(form_id) + "</h2>")
	try:
		forms = Form.objects.get(pk=form_id)
	except Form.DoesNotExist:
		raise Http404("Form does not exist")
	return render(request, 'form/detail.html', {'forms' : forms})	