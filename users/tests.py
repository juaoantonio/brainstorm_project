import re
from django.test import TestCase
from users.models import CustomUser
from django.core.exceptions import ValidationError


class TestCustomUser(TestCase):
    def is_password_hashed(self, password):
        pattern = r"^\w+\$\d+\$[\w+/]+\$.+$"
        return bool(re.match(pattern, password))

    def test_create_user_via_shell(self):
        user = CustomUser.objects.create(
            username="testuser",
            email="test@test.com",
            password="testpassword",
        )

        user.save()

        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@test.com")

    def test_is_password_hashed(self):
        user = CustomUser.objects.create(
            username="testuser",
            email="test@test.com",
            password="testpassword",
        )

        user.save()
        self.assertTrue(self.is_password_hashed(user.password))

    def test_create_user_via_shell_with_invalid_username(self):
        with self.assertRaises(ValidationError):
            user = CustomUser.objects.create(
                username="test user",
                email="testuser@test.com",
                password="testpassword123*",
            )

            user.save()

    def test_create_user_via_shell_with_invalid_email(self):
        with self.assertRaises(ValidationError):
            user = CustomUser.objects.create(
                username="testuser",
                email="testuser.com",
                password="testpassword123*",
            )

            user.save()

    def test_create_user_via_shell_with_invalid_password(self):
        with self.assertRaises(ValidationError):
            user = CustomUser.objects.create(
                username="testuser",
                email="testuser@test.com",
                password="testpas",
            )

            user.save()

    def test_if_user_fields_are_blank(self):
        with self.assertRaises(ValidationError):
            user = CustomUser.objects.create(
                username="",
                email="",
                password="",
            )

            user.save()
