# artist-api

- API Root: http://127.0.0.1:8000/api/
- Retrieve List of Works: http://127.0.0.1:8000/api/works/
- Create a New Work: http://127.0.0.1:8000/api/works/
- Filter Works by Work Type (e.g., 'YT' for Youtube): http://127.0.0.1:8000/api/works?work_type=YT
- Filter Works by Artist Name (e.g., 'John'): http://127.0.0.1:8000/api/works?artist=John
- Register a New User: http://127.0.0.1:8000/api/register/
- Login and Retrieve Authentication Token: You can use the Django REST Framework's built-in ObtainAuthToken view to authenticate users - and obtain tokens. To do this, use the following endpoint:

- POST http://127.0.0.1:8000/api/token/
- The request should contain the username and password as form data. If the     login is successful, the response will include the token, which you can use for subsequent requests by including it in the Authorization header as follows:
Authorization: Token <your_token>

- For testing:
Create a superuser to access the Django admin interface for testing:
python manage.py createsuperuser

- Test the API:
Run the development server and test the API:
python manage.py runserver


