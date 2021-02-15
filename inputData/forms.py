from django import forms

from .models import Input



class CustomInputUserCreationForm(forms.ModelForm):

		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['file'].widget.attrs['class'] = 'btn'
	
	
	class Meta:
		model = Input
		fields = ['title', 'email', 'file']
		labels = {'title':'Название генератора:  ', 'email':'E-mail:  ', 'file': ''}
		