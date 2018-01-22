from django.shortcuts import render,redirect
from Database import models

def index(request):
   return render(request,'home/index.html',{})

def addhome(request):
   if request.user.is_authenticated :
   	return render(request,'home/addhome.html',{})
   return redirect('/admin')

def listhome(request):
   if request.user.is_authenticated :
   	return render(request,'home/listhome.html',{})
   return redirect('/admin')

def filterhome(request):
   if request.user.is_authenticated :
   	return render(request,'home/filterhome.html',{})
   return redirect('/admin')
   
def committee(request):
   return render(request,'home/committee.html',{})
