# fisrt approch 
from django.views.generic.list import ListView  # fisrt approch 
from .models import post_model



class homeview(ListView):
    model = post_model
    template_name = 'posts/post.html'



# second apprch 
from django.views.generic import TemplateView
from django.shortcuts import render
class Homeposts(TemplateView):
    template_name = 'posts/post2.html'
    def get(self,request ):
        model_data = post_model.objects.all()
        return render(request , self.template_name , {'td':model_data})