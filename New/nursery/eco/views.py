from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse(
        """
        <h1> hello welcome to nursery</h1>
        <h5> see all the avaliable species</h5>
        <p>select yourlikes from below</p>
        """
    )
    #