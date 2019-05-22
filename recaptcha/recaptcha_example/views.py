"""Simple views for handle recaptcha v3 example"""

from django.shortcuts import render, redirect
from django.conf import settings
import requests


def index(request):
    """
    simple render index.html
    """

    return render(request, 'index.html', {'site_key': settings.RECAPTCHA_SITE_KEY})


def contact(request):
    """simple handle contact post"""
    if not request.method == 'POST':
        return redirect('/')

    data = request.POST
    name = data.get('name')

    secret_key = settings.RECAPTCHA_SECRET_KEY

    # captcha verification
    data = {
        'response': data.get('g-recaptcha-response'),
        'secret': secret_key
    }
    resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result_json = resp.json()

    print(result_json)

    if not result_json.get('success'):
        return render(request, 'contact_sent.html', {'is_robot': True})
    # end captcha verification

    return render(request, 'contact_sent.html', {'name': name})
