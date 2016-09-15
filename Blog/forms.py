from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(
        label = "Name",
        max_length = 16, 
        error_messages = {
            "required" : "Please enter your name",
            "max_length" : "Name is too long"
        }
    )
    
    email = forms.EmailField(
        label = "Email",
        error_messages = {
            "required" : "Please enter your email",
            "invalid" : "Email is invalid"
        }
    )
    
    content = forms.CharField(
        label = "Content",
        error_messages = {
            "required" : "Please enter the content",
            "max_length" : "Content is too long"
        }
    )
