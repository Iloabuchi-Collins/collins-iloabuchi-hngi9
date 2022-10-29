from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

# CORS HEADERS
# create endpoint to return json data
def endpoint(request):
    data = {
        "slackUsername": 'Collins_I',
        "backend": True,
        "age": 19,
        "bio": "I am a medical student enthusiastic about tech. Let's see how far i go in HNG. Hopefully, i become a finalist."
    }
    response = JsonResponse(data)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response