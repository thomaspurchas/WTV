from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^archive/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    (r'^polls/', include('polls.urls')),
    (r'^booking/', include('booking.urls')),
    url(r'^', include('cms.urls')),

)

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns