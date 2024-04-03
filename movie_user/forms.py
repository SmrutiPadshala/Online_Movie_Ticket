from django import forms
from . import models
# from mysite.movie.models import SetMovie
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        label = "Password",
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    password2 = forms.CharField(
    label = "Confirm Password",
    widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email',]

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            # 'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            # 'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        }


class BookedSeatsForm(forms.Form):
    booked_seats = forms.CharField()



class CheckDateForm(forms.Form):
    date_start = forms.DateField(widget= forms.DateInput(attrs={'name':'date_s'}))
    date_end = forms.DateField(widget = forms.DateInput(attrs={'name':'date_e'}))
    book_date = forms.DateField(widget = forms.DateInput(attrs={'name':'datee'}))
   
    def clean(self):
        all_clean_data = super().clean()
        d_start = all_clean_data['data_start']
        d_end = all_clean_data['date_end']
        datee = all_clean_data['book_date']

        if datee < d_start or datee > d_end:
            raise forms.ValidationError("Wrong date entered")

# class PaymentForm(forms.Form):
#     card_number = forms.CharField(label='Card Number', max_length=16, widget=forms.TextInput)
#     expiration_date = forms.DateField(label='Expiration Date', input_formats=['%m/%Y'], widget=forms.TextInput)
#     cvv = forms.CharField(label='CVV', max_length=3, widget=forms.TextInput)
#     name_on_card = forms.CharField(label='Name on Card', max_length=100, widget=forms.TextInput)
