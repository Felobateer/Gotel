from datetime import datetime

def test_create_hotel(authenticated_client, test_user):
    response = authenticated_client.post('/api/hotel/create/', json = {
        'name': 'New Hotel',
        'address': 'New Location',
        'city': 'New City',
        'email': 'test2@example.com',
        'website': 'http://newhotel.com',
        'img': 'http://newhotel.com/image.jpg',
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
        'description': 'New Description',
        'price': 150.00,
        'rating': 4.0
    })

    print(f"Create Hotel Response: {response.status_code} - {response.data.decode()}")
    assert response.status_code == 201
    assert response.json['message'] == 'Hotel created successfully'

def test_update_hotel(authenticated_client, test_user):
    response = authenticated_client.put('/api/hotel/update/2', hotel = {
        'name': 'Updated Hotel',
        'address': 'New Location',
        'city': 'New City',
        'email': 'test2@example.com',
        'website': 'http://newhotel.com',
        'img': 'http://newhotel.com/image.jpg',
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
        'description': 'New Description',
        'price': 150.00,
        'rating': 4.0
    })
    print(f"Update Hotel Response: {response.status_code} - {response.data.decode()}")
    assert response.status_code == 200
    assert response.json['message'] == 'Hotel updated successfully'

def test_get_hotel(authenticated_client, test_user):
    response = authenticated_client.get('/api/hotel/2')
    print(f"Get Hotel Response: {response.status_code} - {response.data.decode()}")
    assert response.status_code == 200
    assert response.json['hotel_id'] == 2
    assert response.json['name'] == 'Updated Hotel'

def test_delete_hotel(authenticated_client, test_user):
    response = authenticated_client.delete('/api/hotel/delete/2')
    print(f"Delete Hotel Response: {response.status_code} - {response.data.decode()}")
    assert response.status_code == 200
    assert response.json['message'] == 'Hotel deleted successfully'

def test_list_hotels(authenticated_client, test_user):
    response = authenticated_client.get('/api/hotel/list/')
    print(f"List Hotels Response: {response.status_code} - {response.data.decode()}")
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0
    assert response.json[0]['hotel_id'] == 1 

