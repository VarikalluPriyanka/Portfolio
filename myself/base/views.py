from django.shortcuts import render
from django.views.generic import TemplateView
from .models import  About, Project,Education, Internship, Category, Certification,Skills;
from django.http import HttpResponse, HttpResponseNotFound
from wsgiref.util import FileWrapper
import os


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['educations'] = Education.objects.all()
        context['internships'] = Internship.objects.all()
        context['categories'] = Category.objects.all()
        context['projects']= Project.objects.all()
        context['certifications']= Certification.objects.all()
        return context

def download_pdf(request):
    pdf_file_path = os.path.join('base', 'templates', 'VARIKALLU_PRIYANKA_Resume.pdf')

    if os.path.exists(pdf_file_path):
        try:
            with open(pdf_file_path, 'rb') as pdf_file:
                file_wrapper = FileWrapper(pdf_file)
                response = HttpResponse(file_wrapper, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="VARIKALLU_PRIYANKA_Resume.pdf"'
                return response
        except Exception as e:
            return HttpResponse(f"An error occurred while serving the file: {str(e)}", status=500)
    else:
        return HttpResponseNotFound("PDF file not found")

