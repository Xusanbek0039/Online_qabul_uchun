from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
 

# Bosh menu uuchun html sinfi
class HomePageView(TemplateView):
	template_name = 'index.html'

# python cursi uchun html sinfi

class FullPython(TemplateView):
	template_name = 'python_course.html'

# Django cursi uchun html sinf
class DjangoView(TemplateView):
	template_name = 'django.html'

# flask kursi uuchun html sinf

class FlaskView(TemplateView):
	template_name = 'flask.html'