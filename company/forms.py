from django import forms


class CompanyCreate(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={
            'style': 'border-color: blue;',
            'placeholder': 'Write your name here.'
        }
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'style': 'border-color: green;'})
                             )
    phone = forms.CharField(max_length=100, required=True)
    web_site = forms.URLField()
    address = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 100, 'style': 'border-color: orange;'}
    ), help_text='Write here your address.')
