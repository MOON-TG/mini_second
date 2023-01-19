from django.shortcuts import render, redirect
from .models import Info
from django.views.generic import ListView

# Create your views here.

class PostList(ListView):
   model = Info
   ordering = '-pk'
   paginate_by = 1

def createform(request):
   std = Info()
   std.battery= request.GET['battery']
   std.color = request.GET['color']
   std.save()

   return redirect('/')