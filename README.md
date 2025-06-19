# 🏏 HitTrack - Backend (Django REST API)

**HitTrack** is a cricket shot learning and practice tracking platform.  
This repository contains the **Django backend** which powers the API and handles data, authentication, and image uploads.

---

## 🚀 Features

- 🔐 User registration & authentication
- 📚 Shot model with image support
- 📝 Practice log tracking
- 🌐 RESTful API endpoints (Django REST Framework)
- 🛢️ MySQL database integration
- 🖼️ Media/image upload support for cricket shots

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- MySQL
- Pillow (for image handling)
- CORS Headers
- djoser / SimpleJWT (optional for auth)

---

## 📁 Folder Structure
```
```

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/HitTrack-Backend.git
cd HitTrack-Backend
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv env
source env/bin/activate        # On Windows: env\Scripts\activate
pip install -r requirements.txt
Make sure your requirements.txt includes:

text

django
djangorestframework
mysqlclient
pillow
django-cors-headers
```

### 3. Configure Database
In HitTrack/settings.py, update the DATABASES section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hittrack_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Server
```bash
python manage.py runserver
```
The backend API is now running at:
📍 http://localhost:8000/

## 🖼️ Image Upload Support
Make sure you have:

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 🔐 API Authentication (Optional)
If using token-based authentication:

Install djoser or SimpleJWT

Add endpoints for /auth/token/, /auth/users/, etc.

## 📮 API Endpoints
Method	Endpoint	Description
GET	/api/shots/	List all cricket shots
POST	/api/shots/	Add new shot (with image)
GET	/api/practices/	List practice logs
POST	/api/practices/	Log a practice entry

Customize according to your urls.py and views

## 📦 Environment Variables
Create a .env file for sensitive info (if using python-decouple):

```ini
DB_NAME=hittrack_db
DB_USER=root
DB_PASSWORD=your_password
```

## 🔗 Connect with Frontend
Ensure CORS is set up:

```bash
pip install django-cors-headers
In settings.py:

python
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

## 🙋‍♂️ Author
Prathish S
🔗 GitHub 

## 📃 License
This project is open-source and licensed under the MIT License.

```yaml
---

### ✅ How to Use

1. Save the above content as `README.md` in your **backend project root folder**.
2. Run:

```bash
git add README.md
git commit -m "Add backend README"
git push
```









