from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'villaproject.main.views.home', name='home'),
    url(r'^login/$', 'villaproject.main.views.login'),
    url(r'^sign_up/$', 'villaproject.main.views.sign_up'),
    url(r'^logout/$', 'villaproject.main.views.logout_view'),
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)