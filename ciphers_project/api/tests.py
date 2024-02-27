from django.test import TestCase
from .ciphers import caesar_encode

# Create your tests here.
class CiphersTest(TestCase):
    def test_caesar_encoding_1(self):
        plain_text = "hello"
        shift = 1
        expected = "ifmmp"
        output = caesar_encode(plain_text, shift)
        self.assertEqual(output, expected)
    
    def test_caesar_encoding_2(self):
        plain_text = "jui"
        shift = 2
        expected = "lwk"
        output = caesar_encode(plain_text, shift)
        self.assertEqual(output, expected)

    def test_caesar_encoding_2(self):
        plain_text = "fun"
        shift = "1"
        expected = "gvo"
        output = caesar_encode(plain_text, shift)
        self.assertEqual(output, expected)


