from django import forms
from .models import MiniUrl

class MiniURLForm(forms.ModelForm):
	class Meta:
		model = MiniUrl
		fields =('url','pseudo')

