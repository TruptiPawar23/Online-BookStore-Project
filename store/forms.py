from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Review

class RegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'username',
            'password1',
            'password2'
        ]
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class ReviewForm(forms.ModelForm):
    review_star = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    review_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write Your Review'}))

    class Meta:
        model = Review
        fields = [
            'review_star',
            'review_text'
        ]
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    