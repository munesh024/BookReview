from .models import Post_data , Author_Profile , Reader_Profile ,Comment
from django import forms
from .models import User
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class data(forms.ModelForm):
    class Meta:
        model = Post_data
        fields=['title','category','Review']


class author_data(UserCreationForm):
    email = forms.EmailField()
    class Meta :
        model = User
        fields = ['username','email','password1','password2']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_author = True
        if commit:
            user.save()
        return user



class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class UpdateProfileForm(forms.ModelForm):
    mobile = forms.CharField(max_length=12)
    Work_Experience = forms.CharField()
    your_best_work = forms.CharField()
    class Meta:
        model = Author_Profile
        fields = ['mobile','Work_Experience','your_best_work']



#----------------------------------------------------------------------------------------------------------------------#

class Reader_data(UserCreationForm):
    email = forms.EmailField()
    class Meta :
        model = User
        fields = ['username','email','password1','password2']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_reader = True
        if commit:
            user.save()
        return user


class Reader_UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class Reader_UpdateProfileForm(forms.ModelForm):
    Name = forms.CharField()
    mobile = forms.CharField()
    Interest = forms.CharField()
    Location = forms.CharField()
    image = forms.ImageField()
    class Meta:
        model = Reader_Profile
        fields = ['Name','mobile','Interest','Location','image']


class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields = ['content']


