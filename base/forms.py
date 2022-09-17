from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name",'email','phone','dob','password1','password2']
        
class IdentityCardForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['front_img','back_img']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["front_img"].widget.attrs.update({"hidden":True,'id':"front"})
        self.fields['front_img'].label = ''
        self.fields["back_img"].widget.attrs.update({"hidden":True,"id":"back"})
        self.fields['back_img'].label = ''

class UpdateProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['self_image']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["self_image"].widget.attrs.update({"hidden":True,'id':"self_image"})
        self.fields['self_image'].label = ''
