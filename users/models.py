from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField("E-mail", unique=True, blank=False)
    password = models.CharField(_("password"), max_length=128)

    def save(self, *args, **kwargs):
        if self.username == "" or self.email == "" or self.password == "":
            raise ValidationError(_("Username, email and password are required."))

        username_validator = UnicodeUsernameValidator()
        username_validator(self.username)

        email_validator = EmailValidator()
        email_validator(self.email)

        validate_password(self.password)
        self.password = make_password(self.password)

        super().save(*args, **kwargs)
