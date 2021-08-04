from django import forms
from .models import Post, Tag,CustomUser,Comment
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text','category','tag','image')        
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'text': forms.Textarea(attrs={'rows':'5','class': 'form-control'}),
        'category': forms.Select( attrs={'class':'form-control'})}
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),widget=forms.CheckboxSelectMultiple) 

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'password1': forms.PasswordInput(attrs={'class':'form-control'})}

class ProfileUserForm(forms.ModelForm):
    class Meta:
        model= CustomUser
        fields = ("username","email","profileimage")
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
}

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=("name","comment")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'rows':'3','class': 'form-control'}),}
    