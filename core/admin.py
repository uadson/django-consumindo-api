from django.contrib import admin

from django.contrib.auth import admin as auth_admin

from .user_form import UserChangeForm, UserCreationForm

from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
