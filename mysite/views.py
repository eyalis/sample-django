import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Add these to existing imports at the top of the file:
from django.shortcuts import redirect
from django.views.generic import ListView

# Add Twitter functions
from sample-django.control.tweepy_files import twitterApi

# # Replace the existing home function with the one below
# class HomeListView(ListView):
#     """Renders the home page, with a list of all messages."""
#     model = LogMessage

#     def get_context_data(self, **kwargs):
#         context = super(HomeListView, self).get_context_data(**kwargs)
#         return context

def twitter(request):
    twitterSession = twitterApi.TwitterApi()
    sender_id, message_text =twitterSession.retrieveMessages()
    user_name = twitterSession.retrieveUserDataByID(sender_id)

    return render(
        request,
        'hello/twitter.html',
        {
            'sender_id': sender_id,
            'message_text': message_text,
            'user_name': user_name
        }
    )

# def home(request):
#     return render(request, "sample-django/home.html")
