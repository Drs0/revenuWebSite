from dataclasses import field, fields
from pyexpat import model
from statistics import mode
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *






class mailerRegister(UserCreationForm):
    email = forms.EmailField(max_length=80,required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    email.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Mailer
        fields = ['username','email','name','password1','password2']
    def __init__(self, *args,**kwargs):
        super(mailerRegister, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'




class Goal(forms.ModelForm):
    class Meta:
        model = dailyGoal
        fields = ['goal','dayOfMonth','Day','Month','Year']
    def __init__(self, *args,**kwargs):
        super(Goal, self).__init__(*args,**kwargs)
        self.fields['goal'].widget.attrs['class'] = 'form-control'
        self.fields['dayOfMonth'].widget.attrs['class'] = 'form-control'
        self.fields['Day'].widget.attrs['class'] = 'form-control'
        self.fields['Month'].widget.attrs['class'] = 'form-control'
        self.fields['Year'].widget.attrs['class'] = 'form-control'

