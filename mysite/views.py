import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
import importlib  

# Add these to existing imports at the top of the file:
from django.shortcuts import redirect
from django.views.generic import ListView

# Add Twitter functions
# from sample-django.control.tweepy_files import twitterApi
from .control.tweepy_files import twitterApi

def twitter(request):
    twitterSession = twitterApi.TwitterApi()
    sender_id, message_text =twitterSession.retrieveMessages()
    user_name = twitterSession.retrieveUserDataByID(sender_id)

    return render(
        request,
        'twitter.html',
        {
            'sender_id': sender_id,
            'message_text': message_text,
            'user_name': user_name
        }
    )


def signin_form(request):
    return render(
        request,
        'signin_form.html',
        {
            'text': "un texto",
            'title': "mi titulo"
        }
    )

# def home(request):
#     return render(request, "sample-django/home.html")
