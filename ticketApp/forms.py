from django import forms

from .models import *


class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = ('title','requester_email','status','description','locker_num')


class UpdateStatus(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['status']


class UpdateLocker(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['locker_num']