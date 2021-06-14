from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with a email is successful"""
        email = "pushkarasharma11@gmail.com"
        password = "test1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test that email for a new user is normailize""" 
        email = "pushkarasharma@GMAIL.COM"
        user = get_user_model().objects.create_user(
            email = email,
            password = "test123"
        )

        self.assertEqual(user.email,email.lower())

    def test_new_user__invalid_email(self):
        """Test create user with no email raise an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,password="123")

    def test_create_new_super_user(self):
        """Test creating  a new super user""" 
        user = get_user_model().objects.create_superuser(
            email = "test@gmail.com",
            password = "123"
        ) 

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff) 