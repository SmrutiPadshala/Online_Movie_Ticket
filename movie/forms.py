from django import forms
from . import models
from .models import MovieMaster, AdminSide, SetMovie


class AddMovieForm(forms.ModelForm):
    class Meta:
        model = models.MovieMaster
        fields = ('m_name', 'm_desc', 'm_image')

        widgets = {
            'm_name': forms.TextInput(attrs={'class': 'form-control'}),
            'm_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'm_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class SetMovieForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SetMovieForm, self).__init__(*args, **kwargs)
        self.fields['active'].queryset = models.MovieMaster.objects.filter(setmovie__isnull=False)

    class Meta:
        model = models.SetMovie
        fields = ('active', 'start_time', 'end_time', 'show', 'price')

        widgets = {
            'active': forms.Select(attrs={'class': 'form-control', 'style': 'width:300px'}),
            'show': forms.Select(choices=(
                ("1", "Morning"),
                ("2", "Afternoon"),
                ("3", "Evening"),
                ("4", "Night")
            ), attrs={'class': 'form-control', 'style': 'width:300px'}),
            'start_time': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker', 'style': 'width:140px;'}),
            'end_time': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker1', 'style': 'width:140px;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:140px;'})
        }
