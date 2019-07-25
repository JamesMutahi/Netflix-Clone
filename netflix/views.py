from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.conf import settings

import requests

import urllib.request
import urllib
import json
from urllib.parse import quote
from urllib.parse import quote
from .serializer import movieList


# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    if request.method == 'GET':
        category = 'popular'
        url = 'https://api.themoviedb.org/3/movie/' + category + '?api_key='
        response = requests.get( url + settings.MOVIE_API_KEY)
        movieData = response.json()
        movies = movieData['results']



    return render(request, 'home.html', locals())
