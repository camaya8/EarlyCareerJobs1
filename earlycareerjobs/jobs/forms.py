from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ("title", "description", "image", "lat", "lon")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }
        