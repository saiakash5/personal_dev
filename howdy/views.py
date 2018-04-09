#howdy/views.html
from django.shortcuts import render
from django.views.generic import TemplateView
import os
from django.conf import settings
current_file_directory = os.path.dirname(__file__)
file_path = os.path.join(current_file_directory,"../static/Akash_profile.pdf")

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'profile.html', context=None)
    
    
# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"