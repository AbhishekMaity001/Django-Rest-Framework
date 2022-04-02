# Django-Rest-Framework
A simple template for Django Rest Framework


# Steps :
    - pip install django
    - pip install djangorestframework
    
- Django is a python based web framework to build a web applications
- Django rest framework is library within it, basically a toolkit for building API's with Django
    - If you are looking to create a public or a private api or an API to simply serve the data to your own applications.
  Djangorestframework tool will do the job.
```
Step-1 : To create a new project use the command  :
         django-admin startproject <project-name>
         
         NOTE : python manage.py createsuperuser # creates a user with admin level permissions
         
Step-2 : Go inside the settings.py file and add the 'rest-framework' 
         INSTALLED_APPS = ['rest_framework']
         NOTE : its better to keep all the api's in a separate folder of the project

Step-3 : Create a new folder called api in the root directory
         Create __init__.py & views.py file
         Create urs.py file for creating an endpoints for the api (path function is used to set some endpoints & pass the particular view)
         Go to your urls.py file inside the root project folder and add the project urls into this
         path('', include('api.urls'))
         also --> from django.urls import path, include
         
Step-4 : python manage.py runserver  (just to test the current configs)
         open the localhost url after this!
         
Step-5 : Now for getting some real data we will be creating some models and migrating our database
         After we add the data we will serialize the data and output it instead of some static data!
         
Step-6 : Open cmd and create a new project 
         python manage.py startapp <app-name>  # e.g. base
         NOTE : Do add the name in the INSTALLED_APPS = ["base",]
         
Step-7 : go inside the newly created app and add a class in the models.py file
         class Item(models.Model)
         
Step-8 : Once the class is created then do the migrations using below command
         python manage.py makemigrations
         python manage.py migrate  (apply the migrations by migrate command)

Step-9 : Open the cmd and hit
         python manage.py shell  # This will give the cmd interface to get working with the data
         from base.models import Item
         Item.objects.create(name="Item #1")
         Item.objects.create(name="Item #2")
         Item.objects.create(name="Item #3")
         items = Items.objects.all()
         print(items)
         exit()
         
Step-10 : Go to the api folder & add a new file serializers.py
          We need to serialize complex object before rendering. So we need to create a Item class serializer 
          so that the response object can understand.
          
Step-11 : Go to the folder api --> views.py 
          from base.models import Item
          from .serializers import ItemSerializer
          now just query and serialize all the data from the db & return it.
          python manage.py runserver   # to validate
          
Step-12 : Create a new view to add Items from the UI (there are many methods)
          Here we will do it via the Serializer class
          Go and add a addItem(request) function in the api-->views.py file
          Add a new function addItem(request) and add a decorator to it with POST.

Step-13 : Create a new url endpoint of this view inside the api --> urls.py
          path('add/', views.addItem),

Step-14 : Go to the UI url and add a simple post request from there
          {"name" : "Item created from post"}      

```


