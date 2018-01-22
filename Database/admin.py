from django.contrib import admin

from .models import Student,Referee,Professional

class StudentAdmin(admin.ModelAdmin) :
	list_display = ['id', 'name' ,'sex', 'state','club']

class ProfessionalAdmin(admin.ModelAdmin) :
	list_display = ['id', 'name' ,'sex', 'state','club']

class RefereeAdmin(admin.ModelAdmin) :
	list_display = ['id', 'name' , 'state', 'phone']

admin.site.register(Student,StudentAdmin)
admin.site.register(Professional,ProfessionalAdmin)
admin.site.register(Referee,RefereeAdmin)


