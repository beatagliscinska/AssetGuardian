from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomCreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {
            'unique': 'The username you\'ve chosen is already in use. Please select a different username.'
        }


class CustomChangeUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']