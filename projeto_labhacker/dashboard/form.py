from django import forms


class TagForm(forms.Form):
    name_repository = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'readonly': 'readonly',
                'class': 'form-control'}))
    tag = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'data-role': 'tagsinput',
                'class': 'form-control'}),
        required=False)

    def __init__(self, *args, **kwargs):
        tag_values = kwargs.pop('tag_values')
        name = kwargs.pop('name')
        super(TagForm, self).__init__(*args, **kwargs)
        self.fields['tag'].initial = tag_values
        self.fields['name_repository'].initial = name
