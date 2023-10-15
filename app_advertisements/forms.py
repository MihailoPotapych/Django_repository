from django import forms
from .models import Advertisement
from django.forms import ValidationError

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={
                'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={
                'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={
                'class': 'form-control form-control-lg'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0] == '?':
            raise ValidationError('Заголовок не может начинаться с "?"')
        return title
    # title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
    # price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    # auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    # image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))
