from django.urls import path
from . import views    #add the "from . import" to be very specific

# /products (root)
# /products/1/detail...
# /products/new...

urlpatterns = [
    path("", views.index),    #passing reference of function - so do not add () at the end of "index" function
    path("new", views.new_end_point)
]