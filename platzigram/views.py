"""Platzigram Views"""

# Django
from django.http import HttpResponse
import json

# Utilities
from datetime import datetime


def hello_world(req):
    return HttpResponse('The time is {time}'.format(
        time=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))


def sorted_integers(req):
    # Response sorted integers in JSON
    # import pdb; pdb.set_trace() # <--- Esto es un break point debug para hacer debug en consola (El ";" es para no hacer otra linea)
    numbers = sorted([int(i) for i in (req.GET['numbers']).split(',')])
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def say_hi(req, name, age):
    #Return a greeting
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}. Welcome to Platzigram!'.format(name)

    return HttpResponse(message)
