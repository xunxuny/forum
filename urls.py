from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from registration.views import register
from lbforum.accountviews import profile

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotemplate.views.home', name='home'),
    # url(r'^djangotemplate/', include('djangotemplate.foo.urls')),
     url(r'^accounts/register/$',
        register,
        { 'backend': 'lbregistration.backends.simple.SimpleBackend' },
        name='registration_register'),  
    (r'^accounts/', include('registration.backends.default.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('lbforum.urls')),
    url(r'^user/(?P<user_id>\d+)/$', profile, name='user_profile'),
    
    url(r'^attachments/', include('attachments.urls')),
    url(r'^captcha/', include('captcha.urls')),
    
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

