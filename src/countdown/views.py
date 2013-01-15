import os
import json

from django import shortcuts
from django.conf import settings


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

    items = {'containers': get_containers()}
    return shortcuts.render(request, 'countdown/home.html', items)
