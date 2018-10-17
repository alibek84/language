from django import forms

class TagForm(forms.Form):
    tag = forms.CharField(label='tag', max_length=100)
    case = forms.CharField(label='case', max_length=100,required=False)
    verb = forms.CharField(label='verb', max_length=100,required=False)
    pronoun = forms.CharField(label='pronoun', max_length=100,required=False)
    person = forms.CharField(label='person', max_length=100,required=False)
    number = forms.CharField(label='number', max_length=100,required=False)
    poss = forms.CharField(label='poss', max_length=100,required=False)

