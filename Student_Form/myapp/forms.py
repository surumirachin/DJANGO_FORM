from django import forms
from django.core.exceptions import ValidationError
from myapp.models import Student

class ContactForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"

    def clean(self):
        # """
        # Raise `ValidationError` if user didn't provide both name and email.
        # """
        cleaned_data = super().clean() 
        full_Name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        age = cleaned_data.get("age")
        
        if age <18:
             raise ValidationError("age must be greater than 18.")

        if not full_Name and not email:
            raise ValidationError("Please provide name or email.")
        
        return cleaned_data
