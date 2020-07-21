from django import forms

class Choices(forms.Form):
    categoryChoices = (
        ('comedy','comedy'),
        ('romantic', 'romantic'),
        ('mystery', 'mystery'),
        ('horror', 'horror'),
        ('mythology', 'mythology'),
        ('normal', 'normal')
    )
    category = forms.ChoiceField(choices=categoryChoices)