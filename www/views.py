
import json
import pytz
from django.http import HttpResponse
from .api import Twitter
from datetime import datetime
from .utils import get_client_ip
from .models import Tweet, TwitterConfiguration, Country
from django.contrib.gis.geoip2 import GeoIP2


def index(request):
    try:
        # init = request.GET.get('init', '0')
        # uid = request.GET.get('uid', '')
        not_countries = ['uknown', 'localhost']
        ip = get_client_ip(request)
        g = GeoIP2()
        if ip == '127.0.0.1':
            country = 'localhost'
        else:
            country = g.city(ip)
    except Exception:
        country = 'uknown'
    try:
        conf = TwitterConfiguration.objects.first()
        twitter = Twitter()
        if Country.objects.count() > 0 and country not in not_countries and conf.geolocation:
            country_object = Country.objects.filter(
                country_code=country['country_code'].lower()).values('topics', 'languages')
            if len(country_object) > 0:
                topics = country_object[0]['topics'].split()
                languages = country_object[0]['languages'].split()
            else:
                topics = conf.topics.split()
                languages = conf.languages.split()
        else:
            topics = conf.topics.split()
            languages = conf.languages.split()
        twitter.stream(topics, languages)
        tweet = Tweet.objects.latest('twitter_date_created')
        ny_timezone = pytz.timezone("America/New_York")
        ny_datetime = ny_timezone.normalize(tweet.twitter_date_created.astimezone(ny_timezone))
        tweet_object = {
            'name': tweet.name,
            'user': '@{0}'.format(tweet.user),
            'text': tweet.text,
            'date': ny_datetime.strftime('%d/%b/%Y               %H:%M')
        }
        context = json.dumps(tweet_object, ensure_ascii=False)
        return HttpResponse(context, content_type="application/json;charset=utf-8")
    except Exception as e:
        tweet_object = {
            'name': '@Penelope',
            'user': 'Penelope',
            'text': 'I can\'t find you love.',
            'date': datetime.now().strftime('%d/%b/%Y               %H:%M'),
            'error': True,
            'debug': str(e)
        }
        context = json.dumps(tweet_object, ensure_ascii=False)
        return HttpResponse(context, content_type="application/json;charset=utf-8")
