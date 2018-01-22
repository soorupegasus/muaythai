from django import forms



class FilterForm(forms.Form):
    category_choice = [
    ('1','Sub-junior(Cadet)10-11'),
    ('2','Sub-junior(Cadet)12-13'),
    ('3','Junior(Youth)14-15'),
    ('4','Junior(Youth)16-17'),
    ('5','Senior 18-37'),
    ('0','Under age (<10)'),
    ('6','Over age (37+)'),
    ('7','All Categories'),
    ]
    sex_choice = [
    ('Male','Male'),
    ('Female','Female'),
    ]
    
    category = forms.CharField(label="Category",widget = forms.Select(choices = category_choice))
    sex = forms.CharField(label="Sex",widget=forms.Select(choices = sex_choice))
    weight_cat = forms.CharField(label = "Weight Category")
    weight_min = forms.CharField(label="Min Weight")
    weight_max = forms.CharField(label="Max Weight")
    

class ProfessionalForm(forms.Form):
    category_choice = [
    ('0','Professinal Female 48Kg'),
    ('1','Professinal Female 57Kg'),
    ('2','Professinal Female Overweight'),
    ('3','Professinal Male 54Kg'),
    ('4','Professinal Male 57Kg'),
    ('5','Professinal Male 65Kg'),
    ('6','Professinal Male 75Kg'),
    ('7','Professinal Male 85Kg'),
    ('8','Professinal Male 91Kg'),
    ('9','Professinal Male 91+Kg'),
    ]
    category = forms.CharField(label="Category",widget = forms.Select(choices = category_choice))
    
class StateForm(forms.Form):
    state_choice = [
    ('Andra Pradesh', 'Andra Pradesh'),
    (' Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal'),
    ]
    category_choice = [
    ('1','Ameature Fighters'),
    ('2','Professional Fighters'),
    ]
    state = forms.CharField(label="State",widget = forms.Select(choices = state_choice))
    choice = forms.CharField(label="Category",widget = forms.Select(choices = category_choice))
    
class ClubForm(forms.Form):
    category_choice = [
    ('1','Ameature Fighters'),
    ('2','Professional Fighters'),
    ]
    club = forms.CharField(label="Club")
    choice = forms.CharField(label="Category",widget = forms.Select(choices = category_choice))
