from django.contrib.auth.forms import UserCreationForm
from FunApp.models import FunAppUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = FunAppUser
        fields = ('username', 'email', 'profile_pic',)
