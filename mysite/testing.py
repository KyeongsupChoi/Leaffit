import pytest
import requests

# Define the API endpoint URL
url = 'https://kyeongsupchoi.pythonanywhere.com/wendler.html'

# Tests if main domain is up
def test_live():
    # Define the API endpoint URL

    # Make a GET request to the API endpoint
    response = requests.get(url)
    # Check the response status code
    assert str(response) == '<Response [200]>'

