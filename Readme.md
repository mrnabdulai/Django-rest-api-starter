# Django REST API with User Management

This project is a Django REST API implementation with user management functionality, including token-based authentication. It serves as a learning resource for understanding and working with Django Rest Framework (DRF).

## Features

- User registration: Users can sign up and create an account with the API.
- User authentication: Token-based authentication is implemented for user login and API access.
- User profile: Each user has a profile with basic information.
- Password reset: Users can request a password reset if they forget their password.
- API endpoints: The project provides various endpoints for user management, including registration, authentication, profile retrieval, and modification.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/django-rest-api.git
```

2. Change into the project directory:

```bash
cd django-rest-api
```

3. Create a virtual environment and activate it (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run database migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

7. The API should now be accessible at `http://localhost:8000/`. You can test the API endpoints using a tool like [Postman](https://www.postman.com/) or [curl](https://curl.se/).

## Configuration

The project uses the default configuration provided by Django, but you may want to customize certain settings. The main configuration file is `settings.py` located in the project's root directory. You can modify the database settings, email configuration, and other settings as per your requirements.

Make sure to update the `SECRET_KEY` in `settings.py` with your own secret key for security purposes.

## API Endpoints

- **POST /api/users/register**: Register a new user with the API.
- **POST /api/users/login**: Log in with a registered user and obtain an authentication token.
- **POST /api/users/logout**: Log out the currently authenticated user.
- **POST /api/users/reset-password**: Request a password reset email for a user.
- **POST /api/users/reset-password/confirm**: Confirm a password reset request with a new password.
- **GET /api/users/profile**: Retrieve the authenticated user's profile.
- **PUT /api/users/profile**: Update the authenticated user's profile.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

When contributing to this repository, please follow the existing coding style and ensure that your changes are well-documented. Also, make sure to run the tests before submitting a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

The project is built using Django and Django Rest Framework, which are open-source frameworks. Special thanks to the Django and DRF communities for their excellent documentation and support.

## Contact

If you have any questions or suggestions regarding this project, feel free to contact the project owner:

- Name: Abdulai Mohammed Rafiq Nindow
- Email: mohammedrafiq.dev@gmail.com

You can also open an issue in the GitHub repository for bug reports or feature requests.

Happy coding!
