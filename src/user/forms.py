from .models import Person
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Person
        fields = "__all__"


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = Person
        fields = "__all__"
