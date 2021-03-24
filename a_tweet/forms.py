from django import forms
from django.core import validators
from .models import InputData

class AnalyzeTweets(forms.ModelForm):
	class Meta:
		model=InputData
		fields=['topic','no_tweets']
		widgets={
			'topic':forms.TextInput(attrs={'class':'form-control'}),
			'no_tweets':forms.NumberInput(attrs={'class':'form-control'}),
		}

		labels={
			'topic':'Enter Topic',
			'no_tweets':'Number of Tweets to analyze'
		}

