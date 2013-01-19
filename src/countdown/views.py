import datetime
import os
import json

from django import http
from django import shortcuts
from django.conf import settings
from django.core import urlresolvers


def get_containers():
    data_filename = os.path.join(settings.COUNTDOWN_DATA_DIR, 'countdown_data.json')
    with open(data_filename, 'r') as input_file:
        containers = json.load(input_file)

    for container in containers:
        for item in container['items']:
            print item
            if item['num_photos'] > 0:
                item['photo_full_url'] = settings.COUNTDOWN_PHOTO_BASE + 'full_' + item['photo_name']
                item['photo_thumb_url'] = settings.COUNTDOWN_PHOTO_BASE + 'thumb_' + item['photo_name']
            else:
                item['photo_full_url'] = ''
                item['photo_thumb_url'] = ''
    return containers


def home(request):

    context = {
        'containers': get_containers(),
        'current_time': datetime.datetime.now().isoformat(),
        'wedding_time': datetime.datetime(2013, 2, 16, 16, 30, 00).isoformat(),
    }
    return shortcuts.render(request, 'countdown/home.html', context)


def redirect(request):
    return http.HttpResponseRedirect(urlresolvers.reverse(home))
