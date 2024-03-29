from django import forms
from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content', None)
        if len(content) > 240:
            raise forms.ValidationError('content is to long')

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        image = data.get('image', None)
        if content == "":
            contect = None
        if content is None and image is None:
            raise forms.ValidationError('Content or image is required')
        return super().clean(*args, **kwargs)

