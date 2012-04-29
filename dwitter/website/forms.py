from django import forms


class TweetForm(forms.Form):
    message = forms.CharField(max_length=140, widget=forms.Textarea)
