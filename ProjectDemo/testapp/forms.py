from django import forms
from testapp.models import Comments
class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(widget=forms.Textarea)
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('name','email','body')
