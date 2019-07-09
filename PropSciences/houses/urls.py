from django.urls import path
from houses import views

# SET THE NAMESPACE!
app_name = 'houses'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('uploadpics',views.uploadpics,name='uploadpics'),
]
