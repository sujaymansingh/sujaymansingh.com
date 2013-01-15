from django.conf import urls

urlpatterns = urls.patterns('countdown.views',
    urls.url(r'^$', 'home', name='countdown_home')
)
