from fastapi.testclient import TestClient
from teste import app
import os

client = TestClient(app)


test_filename = "test_file.csv"
test_file_content = b"username,inbox\nuser1,inbox\nuser2,inbox\n"

def setup_module(module):
    
    os.makedirs("/tmp/teste-api", exist_ok=True)

def teardown_module(module):

    try:
        os.remove(os.path.join("/tmp/teste-api", test_filename))
    except OSError:
        pass

def test_upload_file():
    response = client.post("/upload/", files={"file": (test_filename, test_file_content)})
    assert response.status_code == 201
    assert response.json() == {"message": "File uploaded successfully"}

def test_list_files():
    response = client.get("/files/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(file["username"] == "test_file" for file in response.json())

def test_get_user_by_size():
    response = client.get(f"/users/{test_filename.split('.')[0]}/size")
    assert response.status_code == 200
    assert "username" in response.json()

def test_get_users_ordered_by_name():
    response = client.get("/users/?order=asc")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_users_inbox():
    response = client.get("/users/inbox/0/100/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

