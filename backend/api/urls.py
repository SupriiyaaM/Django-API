from django.urls import path, include

#from .views import api_home
from . import views

urlpatterns = [
    path('', views.api_home)
    #path('products/', include('products.urls'))
]