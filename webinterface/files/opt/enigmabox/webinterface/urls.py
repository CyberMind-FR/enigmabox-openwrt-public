from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('app.views',

    # language switcher
    url(r'^i18n/setlang/(?P<language>[a-z]+)', 'switch_language'),

    # sites
    url(r'^(?P<program>puppet)/site.pp$', 'puppet_site'),
    url(r'^(?P<program>ansible)/site.yml$', 'puppet_site'),

    # addressbook
    url(r'^addressbook/edit/(?P<addr_id>.*)/$', 'addressbook_edit'),
    url(r'^addressbook/$', 'addressbook'),

    # passwords
    url(r'^passwords/$', 'passwords'),

    # backup & restore
    url(r'^backup/system/$', 'backup_system'),
    url(r'^backup/emails/$', 'backup_emails'),
    url(r'^backup/sslcerts/$', 'backup_sslcerts'),
    url(r'^backup/$', 'backup'),

    # peerings
    url(r'^peerings/new/$', 'peerings_edit'),
    url(r'^peerings/(?P<peering_id>.*)/$', 'peerings_edit'),
    url(r'^peerings/$', 'peerings'),

    # countryselect
    url(r'^countryselect/$', 'countryselect'),

    # ad filter
    url(r'^webfilter/$', 'webfilter'),

    # wlan settings
    url(r'^wlan_settings/scan/$', 'wlan_scan'),
    url(r'^wlan_settings/$', 'wlan_settings'),

    # teletext
    url(r'^teletext/$', 'teletext'),

    # changes
    url(r'^apply_changes/$', 'apply_changes'),

    # puppet output
    url(r'^puppet_output/$', 'puppet_output'),

    # API
    url(r'^api/v1/(?P<api_url>.*)$', 'api_v1'),

    # rest
    url(r'^$', 'home'),
    url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        url(r'static/(?P<path>.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),
        url(r'media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
