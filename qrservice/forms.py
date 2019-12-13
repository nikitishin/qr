from django import forms

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea())
    qr_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Feedback
        fields = ['text', 'name', 'contact']