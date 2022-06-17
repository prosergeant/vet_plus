from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from .models import Teacher


class TeacherCreationForm(UserCreationForm):
    # phone = models.CharField("Номер телефона", max_length=20, blank=True)

    class Meta(UserCreationForm):
        model = Teacher
        fields = ('phone',)


class TeacherChangeForm(UserChangeForm):

    class Meta:
        model = Teacher
        fields = ('phone',)
