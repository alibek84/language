from django import forms

class TagForm(forms.Form):
    lemma = forms.CharField(label='lemma', max_length=100)
    tag = forms.CharField(label='tag', max_length=100)
    case = forms.CharField(label='case', max_length=100,required=False)
    verb = forms.CharField(label='verb', max_length=100,required=False)
    pronoun = forms.CharField(label='pronoun', max_length=100,required=False)
    person = forms.CharField(label='person', max_length=100,required=False)
    number = forms.CharField(label='number', max_length=100,required=False)
    poss = forms.CharField(label='poss', max_length=100,required=False)
    mood = forms.CharField(label='mood', max_length=100,required=False)
    tense = forms.CharField(label='tense', max_length=100,required=False)
    derivation = forms.CharField(label='derivation', max_length=100,required=False)
    prc = forms.CharField(label='prc', max_length=100,required=False)
    gna = forms.CharField(label='gna', max_length=100,required=False)
    gpr = forms.CharField(label='gpr', max_length=100,required=False)
    ger = forms.CharField(label='ger', max_length=100,required=False)
    num = forms.CharField(label='num', max_length=100,required=False)

