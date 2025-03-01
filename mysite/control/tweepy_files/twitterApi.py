# https://docs.tweepy.org/en/latest/getting_started.html#introduction
# https://www.geeksforgeeks.org/python-directmessage-object-in-tweepy/

import tweepy
from django.conf import settings

# Initialize credentials
consumer_key = settings.CONSUMER_KEY
consumer_secret = settings.CONSUMER_SECRET
access_token = settings.ACCESS_TOKEN
access_token_secret = settings.ACCESS_TOKEN_SECRET

class TwitterApi:
 

  def __init__(self):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    self.api = tweepy.API(auth)


  def retrieveMessages(self):
    LastMessage = self.api.list_direct_messages()[0]
    sender_id=LastMessage.message_create['sender_id']
    message_text = LastMessage.message_create['message_data']['text']
    return sender_id, message_text

  def sendMessage(sender_id, text):
    recipient_message_id = LastMessage.message_create[sender_id]
    message_text = "Muchas gracias probando el mensaje"
    api.send_direct_message(recipient_message_id, message_text)

  def retrieveUserDataByID(self, sender_id):
    user = self.api.get_user(sender_id)
    user_name = user.name
    return user_name