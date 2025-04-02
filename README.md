# Travel Agency Web Application

A Django-based travel agency web application with features for booking travel packages, bus tickets, and safety reporting.

## Features

- User authentication and registration
- Travel package booking
- Bus ticket booking
- Safety reporting system
- Weather forecast information
- Admin dashboard
- Moderator management
- Email notifications
- Payment integration

## Technologies Used

- Django
- HTML/CSS/JavaScript
- Bootstrap
- SQLite (development) / PostgreSQL (production)
- Stripe for payments
- Twilio for SMS

## Deployment

This application is configured for deployment on Render.

## Setup Instructions

1. Clone the repository
2. Install dependencies: `pip install -r requirements-render.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the server: `python manage.py runserver`

## Environment Variables

The following environment variables need to be set in Render:

- SECRET_KEY
- DEBUG (set to 'False' in production)
- ALLOWED_HOSTS (comma-separated list)
- DATABASE_URL (provided by Render)
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- TWILIO_ACCOUNT_SID
- TWILIO_AUTH_TOKEN
- TWILIO_PHONE_NUMBER
