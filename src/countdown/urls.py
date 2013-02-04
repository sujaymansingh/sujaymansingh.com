from django.conf import urls

urlpatterns = urls.patterns('countdown.views',
    urls.url(r'^wedding_list$', 'wedding_list', name='countdown_wedding_list'),
    urls.url(r'^notes$', 'notes', name='countdown_notes'),
    urls.url(r'^$', 'home', name='countdown_home')
)
