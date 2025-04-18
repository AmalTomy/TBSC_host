"""
URL configuration for logU project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import CreateCheckoutSessionView
from home.views import payment_success
from home.views import chat_message
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include('home.urls')),
    path('payment-success/', payment_success, name='payment_success'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path('chat_message/', chat_message, name='chat_message'),
]