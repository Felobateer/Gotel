def test_signup(client, init_test_db):
    response = client.post('/api/user/signup/', json={
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane@example.com",
        "password": "pass123"
    })
    assert response.status_code == 201
    assert response.json['message'] == 'User Jane Doe created'

def test_login(client, init_test_db):
    # First, create the user
    client.post('/api/user/signup/', json={
        "first_name": "Test",
        "last_name": "User",
        "email": "test@example.com",
        "password": "testpass"
    })

    response = client.post('/api/user/login/', json={
        'email': 'test@example.com',
        'password': 'testpass'
    })
    assert response.status_code == 200
    assert response.json['message'] == 'User test@example.com logged in'

def test_get_user(authenticated_client, init_test_db):
    response = authenticated_client.get('/api/user/get-user/1/')
    assert response.status_code == 200
    assert response.json['email'] == 'test@example.com'

def test_get_users(authenticated_client, init_test_db):
    response = authenticated_client.get('/api/user/get-all-users/')
    assert response.status_code == 200
    assert 'users' in response.json
    assert isinstance(response.json['users'], list)

def test_edit_user(authenticated_client, init_test_db):
    response = authenticated_client.put('/api/user/edit/1/', json={
        'first_name': 'Updated',
        'last_name': 'User'
    })
    assert response.status_code == 200
    assert "Updated User's data edited successfully" in response.json['message']

def test_delete_user(authenticated_client, init_test_db):
    response = authenticated_client.delete('/api/user/delete-user/1/')
    assert response.status_code == 200
    assert response.json['message'] == 'User with ID 1 deleted successfully'
