"""
URL configuration for ptecnica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from productos import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("create_product/", views.create_product, name="create_product"),
    path("update_product/<int:id>/", views.update_product, name="update_product"),
    path("delete_product/<int:id>/", views.delete_product, name="delete_product"),
    path("product_list/", views.productos, name="product_list"),
    path("marca_list/", views.marcas, name="marca_list"),
    path("create_marca/", views.create_marca, name="create_marca"),
    path("update_marca/<int:id>/", views.update_marca, name="update_marca"),
    path("delete_marca/<int:id>/", views.delete_marca, name="delete_marca"),
]
