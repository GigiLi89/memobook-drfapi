### Security Features
This project is secured by using Django REST permissions and React redirect hook which are protecting the views to write and edit posts and comments. As a user, they can not bypass and change urls to make changes to the site content. They cant access the admin panel either. 

Secret key, Database url and cloudinary url are stored safely in env.py and config vars (Heroku). This will not show in Github repository. 

# Packages Used and more information

- cloudinary: Cloudbased media management for storing, manipulating and delivering media to the Django project. 
- django-cloudinary-storage: Extends Djangos default file storage system to work with Cloudinary. Gives easy storage and access to files from Cloudinary.
- dj-database-url: Enables the DATABASE_URL enviromental variable in the settings file by simplifying the connection to PostgreSQL (CI Database) by parsing the URL and auto-configuring the database settings accordingly.
- django-allauth: Used for account registration, management and authentication with templates, views and forms to handle user auth.
- dj-rest-auth: A Django REST Framework extension for API to handle authentication in DRF projects with endpoints for registration, signin, signout, password, reset and other relatable functions.
- django-filter: Provides a flexible syntax for specifying filters and tegrates seamlessly with DRF.
- djangorestframework-simplejwt: Is a JSON Web Token (JWT) which is an authentication backend for Django REST Framework. It's an easy way to implement roken based authentication in your DRF giving you a secure and statless API authentication.
- pyJWT: JSON Web Token implementation in Python
- django-cors-headers: Adds CORS headers to HTTP responses which enables cross-origin requests from clients JavaSScript app to interact with the Django backend. 
- gunicorn: Used for deploying Django applications and allows it to handle multiple concurrent requests efficiently.
- pillow: Fork of Python Image Library, is a library for image processing in Python with editing functions. 
- psycopg2:A Python adapter for PostgreSQL databases. Allows Django to connect and interact with PostgreSQL databases and making it able to store and retireve data effienctly.
- react-toastify: enables notifications to be shown for user, example: if message was edited/deleted successfully. 

