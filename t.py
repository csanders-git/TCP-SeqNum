import pytest
import requests
def test_1():
	r = requests.get('http://www.example.com')
	print r.text
