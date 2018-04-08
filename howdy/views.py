#howdy/views.html
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'profile.html', context=None)
    
    
# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"