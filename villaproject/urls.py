from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'villaproject.main.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'base.html'}),
    url(r'^logout/$', 'villaproject.main.views.logout_view'),
    # url(r'^villaproject/', include('villaproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)