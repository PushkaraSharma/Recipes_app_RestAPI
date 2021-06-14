from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

class CommandTest(TestCase):

    def test_wait_till_db_ready(self):
        """Test waiting for db when db is available"""
       # override the exact behaviour and just return true
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.return_value, 1)

    #here the nenxt line will just override the actualbehaviour of time.sleep which we
    #  have used in our actual code and just return true so no wait to make test faster 
    @patch('time.sleep',return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""        
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            #five time cause error 6th time true
            gi.side_effect = [OperationalError]*5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)


