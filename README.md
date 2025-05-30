# Gotel
This is a hotel booking site with Django backend using Python programming language and HTML/CSS/JS for the frontend using the framework Vue.js with bootstrap for enhanced UI/UX.

## Core Features
- User registration and authentication
- Search and filter hotels by location, price, and amenities
- Real-time room availability and booking management
- Secure online payment integration
- Booking history and user profile management
- Admin dashboard for hotel and reservation management

## Backend Application

```
asgiref==3.8.1
Django==5.1.1
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
django-redis==5.4.0
redis==5.0.8
django-allauth==0.63.6
psycopg2-binary==2.9.9
django-filter==24.3
drf-yasg==1.21.7
python-decouple==3.8
python-dotenv==1.0.1
gunicorn==23.0.0
whitenoise==6.7.0
PyJWT==2.9.0
pydantic==2.9.2
```
Using this set of dependencies efficiently enables the development of a scalable, secure, and maintainable Django-based web application. Django 5.1.1, paired with Django REST Framework (DRF) 3.15.2, provides a robust foundation for building APIs, while `djangorestframework-simplejwt` facilitates modern, stateless authentication with JWT. `django-allauth` simplifies user authentication workflows, particularly with social login integration. For request filtering, `django-filter` enhances DRF’s capabilities, and `drf-yasg` allows you to auto-generate interactive API documentation with Swagger/OpenAPI, which improves developer collaboration and API usability.

For deployment and performance, `gunicorn` serves as a reliable WSGI HTTP server, and `whitenoise` ensures efficient static file handling. Caching with `django-redis` and `redis` significantly boosts response times and reduces database load, essential for production-readiness. `psycopg2-binary` connects Django to PostgreSQL with high performance, while `python-decouple` and `python-dotenv` keep configuration secure and environment-specific. Finally, `PyJWT` and `pydantic` provide strong tools for secure token handling and data validation, ensuring that both authentication and internal data structures remain clean, safe, and scalable.

