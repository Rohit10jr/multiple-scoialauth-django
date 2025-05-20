<!-- #### Video Tutorial for this project -->
<!-- https://youtu.be/SQ4A7Q6_md8 -->
<!-- git clone https://github.com/andyjud/django-starter.git . && rm -rf .git -->

# Django Starter Project

This project demonstrates how to implement **social authentication** in Django using third-party providers like **Google, GitHub, Facebook**, and **Twitter**. It leverages `django-allauth` or similar packages to integrate OAuth2-based login functionality into a Django web application.

---

## Features

- Login via Google, GitHub, Facebook, and Twitter
- Django admin panel enabled
- Clean and extensible project structure
- Basic UI for login/register and homepage


### Clone the Repository

Make sure you have Git installed, then run:

```bash
git clone https://github.com/andyjud/django-starter.git .
```

## Setup

#### - Create Virtual Environment
###### # Mac
```
python3 -m venv venv
source venv/bin/activate
```

###### # Windows
```
python3 -m venv venv
.\venv\Scripts\activate.bat
```

<br>

#### - Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

<br>

#### - Migrate to database
```
python manage.py migrate
python manage.py createsuperuser
```

<br>

#### - Run application
```
python manage.py runserver
```

<br>

#### - Generate Secret Key ( ! Important for deployment ! )
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```


