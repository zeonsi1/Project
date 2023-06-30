from django import forms

class EmailForm(forms.Form):
    user_email = forms.EmailField(label='tomasgarrido0212@gmail.com')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')