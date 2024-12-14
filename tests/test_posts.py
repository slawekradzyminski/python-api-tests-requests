import pytest
import requests

def test_get_all_posts(posts_url):
    # when
    response = requests.get(posts_url)
    
    # then
    json = response.json()
    assert response.status_code == 200
    assert len(json) == 100
    assert all(isinstance(post, dict) for post in json)
        
def test_get_single_post(posts_url):
    # given
    post_id = 1
    
    # when
    response = requests.get(f"{posts_url}/{post_id}")
    
    # then
    json = response.json()
    assert response.status_code == 200
    assert json["id"] == post_id
    assert "title" in json
    assert "body" in json
    assert "userId" in json
        
def test_create_post(posts_url, sample_post):
    # when
    response = requests.post(posts_url, json=sample_post)
    
    # then
    json = response.json()
    assert response.status_code == 201
    assert json["title"] == sample_post["title"]
    assert json["body"] == sample_post["body"]
    assert json["userId"] == sample_post["userId"]
    assert "id" in json
        
def test_update_post(posts_url, sample_post):
    # given
    post_id = 1
    
    # when
    response = requests.put(f"{posts_url}/{post_id}", json=sample_post)
    
    # then
    json = response.json()
    assert response.status_code == 200
    assert json["id"] == post_id
    assert json["title"] == sample_post["title"]
    assert json["body"] == sample_post["body"]
        
def test_delete_post(posts_url):
    # given
    post_id = 1
    
    # when
    response = requests.delete(f"{posts_url}/{post_id}")
    
    # then
    assert response.status_code == 200 