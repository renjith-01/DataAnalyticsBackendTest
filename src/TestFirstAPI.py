import requests
import os
import pytest
from dotenv import load_dotenv

load_dotenv()

def test_first_api():
    print(os.environ['API_ENDPOINT'])
    assert "a"=="a"

