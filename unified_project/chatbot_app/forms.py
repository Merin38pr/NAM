from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'chat-input', 'placeholder': 'Type your message...'})
    )
