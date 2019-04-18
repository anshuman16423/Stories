from django import forms


class BlogEntry(forms.Form):
    blogTitle = forms.CharField()
    blogPic = forms.FileField()
    blogContent = forms.CharField(widget=forms.Textarea)