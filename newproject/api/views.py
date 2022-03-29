# Response object will take in any python data or any serialized data we pass into it and will render a json data
from rest_framework.response import Response

# Since here we will use the function based apis so import api_view; we will use everywhere this in all our apis
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {'name':'Max', 'age': 25}
    return Response(person)  # Once the python dict is passed into the Response object it will return the json data




