
# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .api import Twitter
from .models import Tweet


def index(request):
    try:
        twitter = Twitter()
        topics = ['love', '#love']
        languages = ['en']
        twitter.stream(topics, languages)
        tweets = Tweet.objects.all()
        tweet = tweets[len(tweets) - 1]
        tweet_object = {'name': tweet.name, 'user': tweet.user, 'text': tweet.text}
        response = '{0}\n{1}\n{2}'.format(tweet.name, tweet.user, tweet.text)
        return HttpResponse(response)
        # return JsonResponse(tweet_object, safe=False)
    except Exception:
        return HttpResponse('DJANGO ERROR')
