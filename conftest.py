import pytest
import requests

@pytest.fixture
def base_url() -> str:
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def posts_url(base_url) -> str:
    return f"{base_url}/posts"

@pytest.fixture
def sample_post() -> dict:
    return {
        "title": "Test post",
        "body": "This is a test post",
        "userId": 1
    } 