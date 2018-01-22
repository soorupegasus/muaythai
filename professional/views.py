from django.shortcuts import render,get_object_or_404
from Database.models import Professional
from datetime import date
def calculate_age(d):
    today = date.today()
    age= today.year - d.year - ((today.month, today.day) < (d.month, d.day))
    return age
    
def index(request):
   if request.user.is_authenticated :
      source = Professional.objects.all()
      for i in source:
   	date=i.dob
   	cat=0
   	cat_name = ''
   	age=calculate_age(date)
   	if i.sex=="Female" : 
   	     if i.weight <= 48 :
   	     	cat=0
   	     	cat_name = "Profesisonal Female 48Kg "
   	     elif i.weight <= 57 : 
   	     	cat=1
   	     	cat_name = "Professional Female 57Kg "
   	     else :
   	     	cat=2
   	     	cat_name = "Professional Female Over Weight (57+)"
   	else :
   	     if i.weight <=54 :
   	     	cat=3
   	     	cat_name = "Professional Male 54 Kg"
   	     elif i.weight <=57 :
   	     	cat=4
   	     	cat_name = "Professional Male 54 Kg"
   	     elif i.weight <=65 :
   	     	cat=5
   	     	cat_name = "Professional Male 65 Kg"
   	     elif i.weight <=75 :
   	     	cat=6
   	     	cat_name = "Professional Male 75 Kg"
   	     elif i.weight <=85 :
   	     	cat=7
   	     	cat_name = "Professional Male  85 Kg"
   	     elif i.weight <=91 :
   	     	cat=8
   	     	cat_name = "Professional Male 91 Kg"
   	     elif i.weight >91 :
   	     	cat=9
   	     	cat_name = "Professional Male 91+ Kg"
   	     
   	q=get_object_or_404(Professional,id=i.id)
   	q.age=age
   	q.category=cat
   	q.category_name=cat_name
   	q.save()
      source = Professional.objects.all()
      context = {'list' : source,}
      return render(request,'professional/list.html',context)
   return redirect('/admin')
