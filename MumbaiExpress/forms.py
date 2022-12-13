from django import forms
from .models import SignupModel,LoginModel,ContactusModel,OrderModel,OrdertableModel





class SignupForm(forms.ModelForm):
    class Meta:
        model=SignupModel
        fields='__all__'

        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter Name','class':'div1','class':'inp'}),
            'username':forms.TextInput(attrs={'placeholder':'Enter User Name','class':'div1','class':'inp',}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter Email','class':'div1','class':'inp'}),
            'contact':forms.NumberInput(attrs={'placeholder':'Enter Contact','class':'inp'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'div1','class':'inp',}),
            'confirmpassword':forms.PasswordInput(attrs={'placeholder':'Enter Confirm Password','class':'div1','class':'inp'}),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model=LoginModel
        fields='__all__'

        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter Username','class':'inp','id':'login'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'inp'}),
        }

class ContactusForm(forms.ModelForm):
    class Meta:
        model=ContactusModel
        fields='__all__'

        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter Name','class':'inpt'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter Email','class':'inpt'}),
            'mobileno':forms.NumberInput(attrs={'placeholder':'Enter Your Mobile No','class':'inpt'}),
            'message':forms.TextInput(attrs={'placeholder':'Put Your Message','class':'inpt'}),
            
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model=OrderModel
        fields='__all__'


    
class OrdertableForm(forms.ModelForm):
    class Meta:
        model=OrdertableModel
        fields='__all__'

        



        