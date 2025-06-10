import pytest
from django.conf import settings
from django.test import Client
from tinydb import TinyDB
from tinydb.storages import MemoryStorage
from datetime import datetime, timedelta
from django.core import mail as django_mail

@pytest.fixture(scope='session')
def tinydb():
    db=TinyDB(storage=MemoryStorage)
    yield db
    db.close()

@pytest.fixture
def test_settings(settings):
    settings.SECRET_KEY = 'test-secret-key'
    settings.EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
    settings.EMAIL_HOST = 'test@example.com'
    settings.DEBUG = True
    return settings

@pytest.fixture
def client(test_settings):
    return Client()

@pytest.fixture
def test_user(tinydb):
    user = {
        'user_id': 1,
        'email': 'test@example.com',
        'password': 'hashed-testpassword',
        'name': 'Test',
        'created_at': datetime.utcnow()
    }
    tinydb.table('users').insert(user)

    hotel = {
        'hotel_id': 1,
        'name': 'Test Hotel',
        'address': 'Test Location',
        'city': 'Test City',
        'email': 'test@example.com',
        'website': 'http://testhotel.com',
        'img': 'http://testhotel.com/image.jpg',
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
        'description': 'Test Description',
        'price': 100.00,
        'rating': 4.5
    }
    tinydb.table('hotels').insert(hotel)
    return user

@pytest.fixture
def authenticated_client(client, test_user):
    client.post('/login/', {
        'email': 'test@example.com',
        'password': 'testpassword'
    })
    return client

@pytest.fixture
def mail_outbox():
    return django_mail.outbox

@pytest.fixture
def mock_smtp(mocker):
    mock = mocker.patch('smtplib.SMTP')
    mock.return_value.starttls.return_value = None
    mock.return_value.login.return_value = None
    mock.return_value.sendmail.return_value = None
    mock.return_value.quit.return_value = None
    return mock

