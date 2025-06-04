GreatKart Django

GreatKart is an advanced e-commerce web application built with the Django framework. This project includes a comprehensive set of features for building a modern online store, such as user authentication, product catalog management, shopping cart, order processing, and PayPal integration.


---

Features

User Authentication – Secure registration, login, and logout

Product Management – Categorized products with details

Shopping Cart – Add, update, and remove items with real-time total calculation

Order Processing – Checkout flow with order tracking

Payment Gateway – PayPal integration for secure transactions

Admin Honeypot – Fake admin login page to trap bots (django-admin-honeypot)

Custom Admin URL – Real admin panel is available at /amin/ instead of default /admin/

Responsive Design – Mobile-friendly user interface



---

Technologies Used

Backend: Django, Python

Frontend: HTML, CSS, JavaScript

Database: SQLite (default)

Payment Gateway: PayPal

Security: django-admin-honeypot for fake admin trap



---

Installation

1. Clone the Repository:

git clone https://github.com/Ebikemeese/greatkart-django.git
cd greatkart-django


2. Create a Virtual Environment:

python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate


3. Install Requirements:

pip install -r requirements.txt


4. Apply Migrations:

python manage.py migrate


5. Create Superuser:

python manage.py createsuperuser


6. Run the Development Server:

python manage.py runserver




---

Accessing the Application

Storefront: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/amin/

Honeypot Trap (Fake Admin): http://127.0.0.1:8000/admin/



---

Configuration

Rename .env-sample to .env and configure environment variables:

Django secret key

PayPal client ID and secret

Debug and allowed hosts
