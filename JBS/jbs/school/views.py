from django.shortcuts import render
from django.views.generic import TemplateView


class Index_View(TemplateView):
    
    template_name = "index.html"


class Course_View(TemplateView):
    
    template_name = "course.html"
    

class Bartender_Course_View(TemplateView):
    
    template_name = 'bartenders_course.html'