# Photo Gallery Web App

## Project Overview

The Photo Gallery Web App is a full-stack Django application that allows users to create an account, log in securely, browse a collection of photos, and interact with them. Users can view photo details, filter photos by tags, like or dislike photos, manage their profiles, and update their account information.

The project is built using Django, PostgreSQL, Tailwind CSS, and Cloudinary for image storage.

---

## Features

### Authentication

- User registration
- User login
- User logout
- Password hashing using Django's authentication system
- Secure authentication and authorization

### User Profile

- View profile information
- Edit profile information
- Update email address
- Change password
- Upload or update profile picture
- Update bio

### Photo Gallery

- Browse all available photos
- View individual photo details
- Display photo title and description
- Display photo tags
- Responsive photo gallery layout

### Photo Interactions

- Like photos
- Dislike photos

### Photo Filtering

- Filter photos using tags
- Easily browse related content

### Responsive Design

- Mobile-friendly interface
- Responsive layout built using Tailwind CSS

---

## Technologies Used

### Backend

- Python 3
- Django

### Frontend

- HTML5
- Tailwind CSS

### Database

- PostgreSQL

### Image Storage

- Cloudinary

### Version Control

- Git
- GitHub

### Deployment

- Render

---

# Project Structure

```
photo_gallery_web_app/
│
├── photo_gallery_project/
├── photo_gallery/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Getting Started

## Clone the Repository

```bash
git clone https://github.com/amorsaralynn08-arch/photo_gallery_web_app.git
```


Navigate into the project directory.

```bash
cd photo_gallery_web_app
```

---

## Create a Virtual Environment

Windows

```bash
python -m venv myenv
```

Linux/macOS

```bash
python3 -m venv myenv
```

---

## Activate the Virtual Environment

Windows Command Prompt

```bash
myenv\Scripts\activate
```

Windows Git Bash

```bash
source myenv/Scripts/activate
```

Linux/macOS

```bash
source myenv/bin/activate
```

---

## Install Dependencies

Install all required packages.

```bash
pip install -r requirements.txt
```

If a requirements file is not available, install the required packages manually.

```bash
pip install django
pip install psycopg2-binary
pip install pillow
pip install cloudinary
pip install django-cloudinary-storage
pip install python-decouple
```

Generate the requirements file afterwards.

```bash
pip freeze > requirements.txt
```

---

# PostgreSQL Configuration

Create a PostgreSQL database.

Example

```
Database Name: photo_gallery
```

Create a PostgreSQL user with the necessary privileges.

---

# Environment Variables

Create a file named `.env` in the root directory.

Example configuration:

```env
SECRET_KEY=your_secret_key

DATABASE_NAME=photo_gallery
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

Never commit the `.env` file to GitHub.

---

# Database Setup

Create migration files.

```bash
python manage.py makemigrations
```

Apply migrations.

```bash
python manage.py migrate
```

Create a superuser.

```bash
python manage.py createsuperuser
```

---

# Running the Application

Start the development server.

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

# Cloudinary Configuration

Create a Cloudinary account.

Obtain the following credentials:

- Cloud Name
- API Key
- API Secret

Add them to your `.env` file.

Example:

```env
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

---

# Authentication

The application uses Django's built-in authentication system.

Users can:

- Register a new account
- Log in
- Log out
- Update profile information
- Change their password

Passwords are securely hashed before being stored in the database.

---

# Gallery Features

Users can:

- Browse all uploaded photos
- View photo details
- Like photos
- Dislike photos
- Filter photos using tags
- View tagged collections

---

# Security

This application follows Django's recommended security practices.

These include:

- Password hashing
- CSRF protection
- Session authentication
- Environment variable management
- PostgreSQL database integration

---

# Deployment

The application can be deployed using Render.

Deployment steps:

1. Push the project to GitHub.
2. Create a PostgreSQL database.
3. Create a Render Web Service.
4. Connect the GitHub repository.
5. Configure all environment variables.
6. Deploy the application.

---

# .gitignore

The following files and folders should be ignored.

```gitignore
# Virtual Environment
myenv/

# Environment Variables
.env

# Python
__pycache__/
*.py[cod]

# SQLite
*.sqlite3

# Media Files
media/

# Static Files
staticfiles/

# IDE
.vscode/
.idea/

# macOS
.DS_Store

# Logs
*.log
```



# License

This project was developed for educational purposes as part of a Django web development assignment.
