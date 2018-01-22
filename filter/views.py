from django.shortcuts import render,redirect,get_object_or_404

from Database.models import Student,Referee,Professional

from .forms import FilterForm,ProfessionalForm,StateForm,ClubForm

def index(request):
    if request.user.is_authenticated :
	form=FilterForm(request.POST or None)
	context={
	"title" : "Normal Events",
	"form" : form
	}
	if form.is_valid():
		cat = form.cleaned_data.get('category')
		sex = form.cleaned_data.get('sex')
		weight_cat = form.cleaned_data.get('weight_cat')
		minw = form.cleaned_data.get('weight_min')
		maxw = form.cleaned_data.get('weight_max')
		iminw=float(minw)
		imaxw=float(maxw)
		cat=int(cat)
		event = ''
		if cat==1:
			event='Sub Junior (Cadet) 10-11'
		elif cat==2:
			event='Sub Junior (Cadet) 12-13'
		elif cat==3:
			event='Junior (Youth) 14-15'
		elif cat==4:
			event='Junior (Youth) 16-17'
		elif cat==5:
			event='Senior 18-37'
		elif cat==0:
			event='Under age (<10)'
		elif cat==6:
			event='Over age (37+)'
		event=event+' '+sex+' '+weight_cat
		if cat<7 :
			instance = Student.objects.filter(category=cat).filter(sex=sex).filter(weight__gte=iminw).filter(weight__lte=imaxw)
		else :
			instance = Student.objects.filter(sex=sex).filter(weight__gte=iminw).filter(weight__lte=imaxw)
			event='All '+sex+' - '+weight_cat
		data = {
			'category' : event,
			'student' : instance,
		}
		return render(request, 'filter/print.html',data)
		
	return render(request, 'filter/filter.html',context)
    
    return redirect('/admin')
    
def referee(request):
    if request.user.is_authenticated :
	instance = Referee.objects.all()
	c = {
	    'ref' : instance,
	}
	return render(request,'filter/referee.html',c)
    return redirect('/admin')
	
def professional(request):
    if request.user.is_authenticated :
	form=ProfessionalForm(request.POST or None)
	context={
	"title" : "Professional Events",
	"form" : form
	}
	if form.is_valid():
		cat = form.cleaned_data.get('category')
		cat=int(cat)
		event = ''
		if cat==0:
			event='Professional Female 48Kg'
		elif cat==1:
			event='Professional Female 57Kg'
		elif cat==2:
			event='Professional Female Over weight (57+Kg)'
		elif cat==3:
			event='Professional Male 54Kg'
		elif cat==4:
			event='Professional Male 57Kg'
		elif cat==5:
			event='Professional Male 65Kg'
		elif cat==6:
			event='Professional Male 75Kg'
		elif cat==7:
			event='Professional Male 85Kg'
		elif cat==8:
			event='Professional Male 91Kg'
		elif cat==9:
			event='Professional Male 91+Kg'
		
		instance = Professional.objects.filter(category=cat)
		data = {
			'category' : event,
			'student' : instance,
		}
		return render(request, 'filter/print.html',data)
		
	return render(request, 'filter/proffilter.html',context)
    return redirect('/admin')
	
def state(request):
    if request.user.is_authenticated :
	form=StateForm(request.POST or None)
	context={
	"title" : "Filter by State",
	"form" : form
	}
	if form.is_valid():
		state = form.cleaned_data.get('state')
		choice = form.cleaned_data.get('choice')
		choice=int(choice)
		if choice == 1:
			instance = Student.objects.filter(state=state)
			state=state+' State - '+'Ameature Fighters'
		else :
			instance = Professional.objects.filter(state=state)
			state=state+' State - '+'Professional Fighters'
		data = {
			'category' : state,
			'student' : instance,
		}
		return render(request, 'filter/scprint.html',data)
		
	return render(request, 'filter/statefilter.html',context)
    return redirect('/admin')


def club(request):
    if request.user.is_authenticated :
	form=ClubForm(request.POST or None)
	context={
	"title" : "Filter by Club",
	"form" : form
	}
	if form.is_valid():
		club = form.cleaned_data.get('club')
		choice = form.cleaned_data.get('choice')
		choice=int(choice)
		if choice == 1:
			instance = Student.objects.filter(club=club)
			club=club+' Club - '+'Ameature Fighters'
		else :
			instance = Professional.objects.filter(club=club)
			club=club+' Club -  '+'Professional Fighters'
		data = {
			'category' : club,
			'student' : instance,
		}
		return render(request, 'filter/scprint.html',data)
		
	return render(request, 'filter/clubfilter.html',context)
    return redirect('/admin')	

