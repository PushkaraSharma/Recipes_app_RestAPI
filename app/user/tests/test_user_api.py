from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTest(TestCase):
    """Test public users APIs """
    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_successful(self):
        """Test creating the user with valid payload"""
        payload  = {
            'email':'test12@gmail.com',
            'password':'1234',
            'name':'pushkara'
        }
        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        #checking if after creating the user password is saved in db
        self.assertTrue(user.check_password(payload['password']))
        #check password in not in response
        self.assertNotIn('password',res.data)

    def test_create_duplicate(self):
        """Test creating user that already exist """
        payload = {
            'email':'test123@gmail.com',
            'password':'123',
            'name':'pk'

        }        
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL,payload) 

        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)

    def test_password_length(self):
        """Password should have length more than 4 chars"""  
        payload = {
            'email':'test1@gmail.com',
            'password':'wq',
            'name':'pks'
            }     
        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        #check if user is not created for above thing
        user_exists = get_user_model().objects.filter(
            email = payload['email']
        ).exists()
        #it should not be created
        self.assertFalse(user_exists)
