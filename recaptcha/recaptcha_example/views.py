"""Simple views for handle recaptcha v3 example"""

from django.shortcuts import render, redirect
from django.conf import settings


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

    return render(request, 'contact_sent.html', {'name': name})
